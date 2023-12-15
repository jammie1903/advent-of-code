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
    const sequentialGroups = possibleSpringGroups.reduce((acc, group) => {
      const unknowns = Array(group.length)
        .fill()
        .map((_i, index) => index)
        .filter(index => group[index] === "?");
      let possibilities = [group];
      unknowns.forEach(dataIndex => {
        possibilities = possibilities.reduce((acc, entry) => {
          acc.push(entry.substring(0, dataIndex) + "." + entry.substring(dataIndex + 1));
          acc.push(entry.substring(0, dataIndex) + "#" + entry.substring(dataIndex + 1));
          return acc;
        }, []);
      });
      const possibilityPatterns = possibilities.map(p => p.split(/\.+/).filter(Boolean).map(s => s.length).join(","));
      const flattenedPatterns = possibilityPatterns.reduce((possAcc, pattern) => {
        possAcc[pattern] ||= 0
        possAcc[pattern]++;
        return possAcc;
      }, {})
      const returnObject = {};
      Object.entries(acc).forEach(([partialPattern, count]) => {
        Object.entries(flattenedPatterns).forEach(([possibilityPattern, count2]) => {
          const combinedPattern = [partialPattern, possibilityPattern].filter(Boolean).join(",");
          if (pattern.startsWith(combinedPattern)) {
            returnObject[combinedPattern] ||= 0;
            returnObject[combinedPattern] += count * count2;
          }
        })
      })
      console.log(returnObject)
      return returnObject
    }, { "": 1 });
    console.log(sequentialGroups);
    total += sequentialGroups[pattern] || 0;
    // total += possibilities.filter(p =>
    //   p.split(/\.+/).filter(Boolean).map(s => s.length).join(",") === pattern
    // ).length
  });
  return total;
};
