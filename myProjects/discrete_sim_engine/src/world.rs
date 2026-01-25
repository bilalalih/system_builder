use crate::{agent::Agent, resource::Resource, position::Position};

#[derive(Debug)]
pub struct World {
    pub width: i32,
    pub height: i32,
    pub agents: Vec<Agent>,
    pub resources: Vec<Resource>,
    // next_id: u64,
}

impl World {
    pub fn new(width: i32, height: i32) -> Self {
        Self {
            width,
            height,
            agents: Vec::new(),
            resources: Vec::new(),
        }
    }

    pub fn spawn_agents(&mut self, count: usize) {
        // Hardcode deterministic positions for now
        for i in 0..count {
            let pos = Position { x: i as i32 % self.width, y: (i as i32 / self.width) % self.height };
            self.agents.push(Agent::new(i as u64, pos));
        }
    }

    // More spawn_resources, update, etc.
}