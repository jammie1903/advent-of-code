module.exports = input => {
  const lines = input
    .split("\n")
    .filter(Boolean)
    .map(line => {
      const [data, pattern] = line.split(" ");
      return {
        data: Array(5).fill(data).join("?"),
        pattern: Array(5).fill(pattern).join(",")
      };
    });
  let total = 0;
  lines.forEach(({ data, pattern }) => {
    const possibleSpringGroups = data.split(/\.+/).filter(Boolean);
    console.log(pattern, possibleSpringGroups)
    const highestGroupSize = pattern.split(",").map(Number).reduce((a, b) => Math.max(a, b))
    console.log({highestGroupSize})
    let comparison = "startsWith"

    const sequentialGroups = possibleSpringGroups.reduce((acc, group) => {
      const sectionLengths = group.split("?").map(s => s.length);
      console.log(sectionLengths)
      let possibilities = { [sectionLengths[0] || ""]: 1 }
      sectionLengths.slice(1).forEach(l => {
        const newPoss = {}
        Object.entries(possibilities).forEach(([p, count]) => {
          const arr = p.split("");
          const copy = [...arr];
          if (/\d/.test(copy[copy.length - 1])) {
            arr.push(",")
            copy[copy.length - 1] = Number(copy[copy.length - 1]) + l + 1;
          } else {
            copy.push(l + 1);
          }

          [arr, copy].forEach(sequence => {
            const endsInNumber = /\d/.test(sequence[sequence.length - 1])
            if (endsInNumber && Number(sequence[sequence.length - 1]) > highestGroupSize) return;
            const str = sequence.join("");
            const compString = endsInNumber ? str.substring(0, str.length - 1) : str;
            if(pattern[comparison](compString)) {
              newPoss[str] ||= 0;
              newPoss[str] += count;
            }
          })
        })
        possibilities = newPoss;
        // possibilities = possibilities.filter(p => {
        //   if(p[p.length - 1] > highestGroupSize) return false;
        //   const readyString = p
        //     .slice(0, p.length - 1)
        //     .join(",")
        //   return pattern[comparison](readyString.substring(0, readyString.length - 2));
        // })
      });

      possibilities = Object.entries(possibilities).reduce((acc, [sequence, count]) => {
        const trimmedSequence = sequence.endsWith(",") ? sequence.substring(0, sequence.length - 1) : sequence;
        acc[trimmedSequence] ||= 0;
        acc[trimmedSequence] += count;
        return acc;
      }, {})
      // console.log(possibilities)


      // possibilities = possibilities.map(p => p.join(","));
      // let possibilities = [[sectionLengths[0]]]
      // sectionLengths.slice(1).forEach(l => {
      //   const originalPossibilities = [...possibilities]
      //   originalPossibilities.forEach(p => {
      //     const copy = [...p];
      //     if(l)
      //       p.push(l)
      //     copy[copy.length - 1] += l + 1
      //     possibilities.push(copy)
      //   })
      //   possibilities = possibilities.filter(p => {
      //     if(p[p.length - 1] > highestGroupSize) return false;
      //     const readyString = p
      //       .slice(0, p.length - 1)
      //       .join(",")
      //     return pattern[comparison](readyString.substring(0, readyString.length - 2));
      //   })
      // })
      // possibilities = possibilities.map(p => p.join(","));

      // let possibilities = [group];
      // unknowns.forEach(dataIndex => {
      //   possibilities = possibilities.reduce((acc, entry) => {
      //     acc.push(entry.substring(0, dataIndex) + "." + entry.substring(dataIndex + 1));
      //     acc.push(entry.substring(0, dataIndex) + "#" + entry.substring(dataIndex + 1));
      //     return acc;
      //   }, []);
      //   possibilities = possibilities.filter(p => {
      //     const readyString = p
      //       .substring(0, dataIndex + 1)
      //       .split(/\.+/)
      //       .filter(Boolean)
      //       .map(s => s.length)
      //       .join(",");
      //     return pattern[comparison](readyString.substring(0, readyString.length - 2));
      //   });
      // });

      // const unknowns = Array(group.length)
      //   .fill()
      //   .map((_i, index) => index)
      //   .filter(index => group[index] === "?");
      // let possibilities = [group];
      // unknowns.forEach(dataIndex => {
      //   possibilities = possibilities.reduce((acc, entry) => {
      //     acc.push(entry.substring(0, dataIndex) + "." + entry.substring(dataIndex + 1));
      //     acc.push(entry.substring(0, dataIndex) + "#" + entry.substring(dataIndex + 1));
      //     return acc;
      //   }, []);
      //   possibilities = possibilities.filter(p => {
      //     const readyString = p
      //       .substring(0, dataIndex + 1)
      //       .split(/\.+/)
      //       .filter(Boolean)
      //       .map(s => s.length)
      //       .join(",");
      //     return pattern[comparison](readyString.substring(0, readyString.length - 2));
      //   });
      // });
      // const possibilityPatterns = possibilities.map(p => p.split(/\.+/).filter(Boolean).map(s => s.length).join(","));
      // const flattenedPatterns = possibilities.reduce((possAcc, pattern) => {
      //   possAcc[pattern] ||= 0
      //   possAcc[pattern]++;
      //   return possAcc;
      // }, {})
      if(Object.keys(acc).length === 0) {
        acc[""] = 1;
      }
      const returnObject = {};
      Object.entries(acc).forEach(([partialPattern, count]) => {
        Object.entries(possibilities).forEach(([possibilityPattern, count2]) => {
          const combinedPattern = [partialPattern, possibilityPattern].filter(Boolean).join(",");
          if (pattern.startsWith(combinedPattern)) {
            returnObject[combinedPattern] ||= 0;
            returnObject[combinedPattern] += count * count2;
          }
        })
      })
      comparison = "includes"
      return returnObject
    }, { });
    console.log("result", sequentialGroups[pattern])
    total += sequentialGroups[pattern] || 0;
    // total += possibilities.filter(p =>
    //   p.split(/\.+/).filter(Boolean).map(s => s.length).join(",") === pattern
    // ).length
  });
  return total;
};
