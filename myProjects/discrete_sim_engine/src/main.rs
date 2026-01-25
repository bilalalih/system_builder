mod position;
mod agent;
mod resource;
mod world;
mod config;
mod utils;
mod rules;

use world::World;

fn main() {
    let mut world = World::new(20, 20);
    world.spawn_agents(30);
    // world.spawn_resources(15);

    for tick in 0..10 {  // Small for testing
        // world.update();  // Implement later
        println!("Tick {}: {} agents", tick, world.agents.len());
    }
}