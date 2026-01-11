const int num_particles = 2;
const int ticks = 20;
const int HEIGHT = 10;
const int WIDTH = 10;
#include <iostream>
#include <random>
#include <vector>
using namespace std;

class Particle{
    public:
        double x, y;     // Position
        double vx, vy;   // Velocity
        Particle(double x, double y, double vx, double vy):
            x(x), y(y), vx(vx), vy(vy) { }
        ~Particle() {}
        
        void update_position() {
            x += vx;
            y += vy;
            if (x < 0) x = 0, vx = -vx; // Bounce off walls
            if (x > WIDTH) x = WIDTH, vx = -vx;
            if (y < 0) y = 0, vy = -vy; // Bounce off walls
            if (y > HEIGHT) y = HEIGHT, vy = -vy;
        }
};

int main(){
    
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<double> pos(0.0, WIDTH);
    uniform_real_distribution<double> vel(-0.5, 0.5);

    vector<Particle> particles;

    for(int i = 0; i < num_particles; i++){
        particles.emplace_back(pos(gen), pos(gen), vel(gen), vel(gen));
        particles[i].update_position();
        cout << "Particle " << i << ": Position(" << particles[i].x << ", " << particles[i].y << ")\n";
    }

    for(int t = 0; t < ticks; t++){

        cout << "Tick " << t << ":\n";

        for(int i = 0; i < num_particles; i++){
            particles[i].update_position();
            cout << "Particle " << i << ": Position(" << particles[i].x << ", " << particles[i].y << ")\n";
        }

        for(int i = 0; i < particles.size(); i++){
            for(int j = i + 1; j < particles.size(); j++){
                double dx = particles[i].x - particles[j].x;
                double dy = particles[i].y - particles[j].y;
                double dist = sqrt(((dx*dx) + (dy*dy)));
                if (dist < 1.5) {
                    swap(particles[i].vx, particles[j].vx);
                    swap(particles[i].vy, particles[j].vy);
                    cout << "Collision detected between Particle " << i << " and Particle " << j << "!\n";
                }
            }
        } 
    }
}