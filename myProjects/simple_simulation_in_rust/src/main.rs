use std::io;

struct Postion(i32, i32);
struct Agent{
    pos: Postion
}

impl Agent{
    fn new(x: i32, y: i32) -> Self {
        Self{
           pos: Postion(x, y)
        }
    }
}

fn main() {
    println!("Direction to move(0, 1, 2, 3): ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut entity = Agent::new(3, 4);
    let num: i32 = input.trim().parse().expect("Not a number");
    let dir = num %4;
    match dir {
        0 => {entity.pos.0 += 1;
              println!("Right")},
        1 => {entity.pos.0 -= 1;
               println!("Left")},
        2 => {entity.pos.1 += 1;
                println!("Up")},
        3 => {entity.pos.1 -= 1;
            println!("Down")},
        _ => {println!("No direction")}
    }

    let Agent{pos: Postion(x1, y1)} = entity;
    println!(" Current position of agent: x:{}, y:{}", x1, y1);
}
