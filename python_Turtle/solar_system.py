
import turtle
import math
import random

# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.setup(width=900, height=750)
screen.title("Solar System Simulation")
screen.bgcolor("black")
screen.tracer(0)

# Ensure a normal, resizable window
root = screen.getcanvas().winfo_toplevel()
root.resizable(True, True)
root.state("normal")
root.geometry("900x750+50+30")

# ---------------- BACKGROUND STARS ----------------
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.speed(0)

for _ in range(100):
    x = random.randint(-430, 430)
    y = random.randint(-340, 340)

    stars.goto(x, y)
    stars.dot(random.randint(1, 3), "white")

# ---------------- DRAW ORBITS ----------------
def draw_orbit(radius):
    orbit = turtle.Turtle()
    orbit.hideturtle()
    orbit.speed(0)
    orbit.penup()
    orbit.color("#303030")
    orbit.goto(0, -radius)
    orbit.pendown()
    orbit.circle(radius)

# ---------------- SUN ----------------
sun = turtle.Turtle()
sun.shape("circle")
sun.color("#FFD700")
sun.shapesize(2.5)
sun.penup()
sun.goto(0, 0)
sun.speed(0)

# Sun glow effect
glow = turtle.Turtle()
glow.hideturtle()
glow.penup()
glow.goto(0, -24)
glow.pendown()
glow.color("#FF8C00")
glow.pensize(2)
glow.circle(24)

# ---------------- PLANET DATA ----------------
# name, color, orbit radius, size, speed
planets_data = [
    ("Mercury", "#AAAAAA", 45, 0.4, 4.7),
    ("Venus",   "#E5B567", 75, 0.6, 3.5),
    ("Earth",   "#3399FF", 105, 0.7, 2.9),
    ("Mars",    "#FF5533", 135, 0.5, 2.4),
    ("Jupiter", "#D9A066", 170, 1.3, 1.3),
    ("Saturn",  "#E6D39B", 210, 1.1, 0.9),
    ("Uranus",  "#66DDDD", 250, 0.9, 0.6),
    ("Neptune", "#4466FF", 290, 0.9, 0.4),
]

planets = []

# ---------------- CREATE PLANETS ----------------
for name, color, radius, size, speed in planets_data:

    draw_orbit(radius)

    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.speed(0)

    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.color("white")

    planets.append({
        "name": name,
        "turtle": planet,
        "label": label,
        "radius": radius,
        "angle": random.randint(0, 359),
        "speed": speed,
    })

# ---------------- SATURN RING ----------------
saturn_ring = turtle.Turtle()
saturn_ring.hideturtle()
saturn_ring.penup()
saturn_ring.color("#C9B37E")
saturn_ring.pensize(2)

# ---------------- ANIMATION ----------------
paused = False

def animate():
    if not paused:
        for p in planets:
            p["angle"] = (p["angle"] + p["speed"]) % 360

            angle = math.radians(p["angle"])
            x = p["radius"] * math.cos(angle)
            y = p["radius"] * math.sin(angle)

            p["turtle"].goto(x, y)

            # Update planet name
            p["label"].clear()
            p["label"].goto(x, y + 12)
            p["label"].write(
                p["name"],
                align="center",
                font=("Arial", 8, "normal")
            )

            # Draw Saturn's ring around its current position
            if p["name"] == "Saturn":
                saturn_ring.clear()
                saturn_ring.penup()
                saturn_ring.goto(x - 12, y - 3)
                saturn_ring.pendown()
                saturn_ring.setheading(0)
                saturn_ring.circle(15, steps=30)

    screen.update()
    screen.ontimer(animate, 30)

# ---------------- CONTROLS ----------------
def toggle_pause():
    global paused
    paused = not paused

def close_program():
    screen.bye()

screen.listen()
screen.onkey(toggle_pause, "space")
screen.onkey(close_program, "Escape")

# ---------------- START ----------------
animate()
screen.mainloop()
