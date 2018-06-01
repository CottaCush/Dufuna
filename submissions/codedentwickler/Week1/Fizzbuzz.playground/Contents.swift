//: Playground - noun: a place where people can play

import Foundation

func fizzbuzz(_ i: Int) -> String {
    let result = (i % 3, i % 5)
    switch result {
        case (0, 0):
            return "FizzBuzz"
        case (0, _):
            return "Fizz"
        case (_, 0):
            return "Buzz"
        default:
            return String(i)
    }
}

for number in 1...100 {
    print(fizzbuzz(number))
}
