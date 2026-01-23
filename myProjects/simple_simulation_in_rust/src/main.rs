use std::io;
use rand::Rng;

struct Position(i32, i32);
struct Agent{
    pos: Position
}

impl Agent{
    fn new(x: i32, y: i32) -> Self {
        Self{
           pos: Position(x, y)
        }
    }
}

fn sequence(num: i32, len: i32) -> Result<Vec<i32>, &'static str>{
    let mut seq_num = vec![];
    let mut rng = rand::thread_rng();
    if len > 0{
        for _i in 0..len {
            let random_number: i32 = rng.gen_range(1..=10);
            seq_num.push(num + random_number);
        }
    } else{
        return Err("Length must be greater than 0");
    }
    return Ok(seq_num);
}

fn main() {
    println!("Direction to move(0, 1, 2, 3): ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut entity = Agent::new(3, 4);
    let len = 3;
    let num: i32 = input.trim().parse().expect("Not a number");
    if let Ok(numbers) = sequence(num, len) {
        for nume in &numbers {
          println!("Generated number: {}", nume);
          let dir = nume %4;
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
        }
    } else {
        println!("Error generating sequence");
    }

    let Agent{pos: Position(x1, y1)} = entity;
    println!(" Current position of agent: x:{}, y:{}", x1, y1);
}
