use crate::position::Position;

#[derive(Clone, Debug)]
pub struct Agent {
    pub id: u64,
    pub pos: Position,
    pub energy: u32,
    // goal: Goal, ... later
}

impl Agent {
    pub fn new(id: u64, pos: Position) -> Self {
        Self { id, pos, energy: 50 }
    }

    // Methods like move_toward later
}