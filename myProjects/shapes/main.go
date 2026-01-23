package main

import (
	"fmt"
	"shapes/shape"
)

func main() {
	c := shape.Circle{Radius: 7.2}

	shape.PrintArea(c)

	c2 := &shape.Circle{Radius: 4}
	// Go automatically dereferences
	shape.PrintArea(c2)
	fmt.Println(*c2)
}
