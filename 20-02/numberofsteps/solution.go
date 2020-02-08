package main

import "fmt"

func numberOfSteps(num int) int {
	count := 0
	for num > 0 {
		if num%2 == 0 {
			num = num / 2
		} else {
			num -= 1
		}
		count++
	}
	return count
}

func main() {
	fmt.Println(numberOfSteps(1000000))
}
