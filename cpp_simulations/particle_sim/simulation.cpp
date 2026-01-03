#include <iostream>

const int WIDTH = 40, HEIGHT = 20;
constexpr int STEPS = 3;

struct Particle{
    float x, y;
    float vx, vy;
};

void update(Particle& p){
    if (p.x > 0 && p.x <= WIDTH && p.y > 0 && p.y <= HEIGHT){
        p.x += p.vx;
        p.y += p.vy;
    }
}

int main(){
    Particle quark;
    quark.x = 1; quark.y = 2; quark.vx = 1; quark.vy = 0.1;
    for (size_t i = 0; i < STEPS; i++)
    {
        update(quark);
        std::cout << "Position (x, y): (" << quark.x << ", " << quark.y << ")." << '\n';
    }
    
}