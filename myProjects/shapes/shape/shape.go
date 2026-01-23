package shape

import (
	"fmt"
)

// Interface: Set of method signatures
// types implement by defining methods
type Shape interface {
	Area() float64
}

type Circle struct {
	Radius float64
}

// Circle struct reciever function implement Area
func (c Circle) Area() float64 { return 3.14 * c.Radius * c.Radius }

func PrintArea(s Shape) {
	fmt.Println(s.Area())
}

type Rectangle struct{ Length float64 }

// Rectangle struct reciever function implement Area
func (r Rectangle) Area() float64 { return r.Length * r.Length }

// Empty interface(interface{}): Any type.
