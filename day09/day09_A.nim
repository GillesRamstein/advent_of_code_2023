import std/strformat
import std/strutils
import std/sequtils

proc load_example(): seq[string] =
  result = slurp("example_input.txt").splitLines()
  if result[^1] == "":
    result.setLen(result.len - 1)

proc load_input(): seq[string] =
  result = slurp("input.txt").splitLines()
  if result[^1] == "":
    result.setLen(result.len - 1)

proc sumInterpolatedValues(lines: seq[string]): int =
  for line in lines:
    var values = line.split(" ").map(parseInt)
    var endValues: seq[int] = @[values[^1]]
    while not values.allIt(it == 0):
      var tmp: seq[int] = @[]
      for i in 0..values.len-2:
        tmp.add(values[i+1]-values[i])
      values = tmp
      endValues.add(values[^1])
    result += endValues.foldl(a+b, 0)

proc writeResult(result: int) =
  writeFile("result_A.txt", $result)

proc main() =
  let interpSumExample: int = sumInterpolatedValues(static load_example())
  assert interpSumExample == 114, fmt"Failed example_input_A: {interpSumExample}!=114"

  let interpSum: int = sumInterpolatedValues(static load_input())
  echo fmt"Sum of interpolated values: {interpSum}"
  writeResult(interpSum)

when isMainModule:
  main()
