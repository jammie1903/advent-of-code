module.exports = input => {
  const lines = input.split("\n").filter(Boolean).map(line => {
    const [data, pattern] = line.split(" ");
    return { data, pattern }
  })
  let total = 0;
  lines.forEach(({ data, pattern }) => {
    const unknowns = Array(data.length).fill().map((_i, index) => index)
      .filter(index => data[index] === "?")
    let possibilities = [data]

    unknowns.forEach((dataIndex, index) => {
      possibilities = possibilities.reduce((acc, entry) => {
        // console.log(entry)
        acc.push(entry.substring(0, dataIndex) + "." + entry.substring(dataIndex + 1))
        acc.push(entry.substring(0, dataIndex) + "#" + entry.substring(dataIndex + 1))
        return acc
      }, [])
    })

    total += possibilities.filter(p =>
      p.split(/\.+/).filter(Boolean).map(s => s.length).join(",") === pattern
    ).length
  })
  return total
}
