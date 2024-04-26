import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from air_cl import Air
from space_cl import Space, sq_off, c_diff
from air_cl import Particle, resy, resx

dim = 0.01


# Initialize Space
space = Space(dim, dim, 7500)
space.setmol()
space.setmaxwell()
space.update()

# Get initial scatter data
bxscat = space.getscatx()
byscat = space.getyscat()

# Create figure and axis
fig, ax = plt.subplots()
fig2, (ax2, ax3) = plt.subplots(1, 2)
ax2.set_xlim(0, dim)
ax2.set_ylim(0, dim)
plt.ylabel("D")
plt.xlabel("N")

sc = ax.scatter(bxscat, byscat)
he = ax.scatter(space.get_he_cord()[0], space.get_he_cord()[1], color = "red")

pl = ax2.scatter(resx, resy)
pl2 = ax3.scatter(np.linspace(0, len(c_diff), len(c_diff)), c_diff)
ax3.set_xlim(0, 1000)
ax3.set_ylim(0, 10)

# Update function for animation
def update(frame):
    space.update()  # Update molecule positions
    bxscat = space.getscatx()  # Get updated x coordinates
    byscat = space.getyscat()  # Get updated y coordinates
    sc.set_offsets(np.c_[bxscat, byscat])  # Update scatter plot data
    he.set_offsets(np.c_[space.get_he_cord()[0], space.get_he_cord()[1]])
    pl.set_offsets(np.c_[resx, resy])
    pl2.set_offsets(np.c_[np.linspace(0, len(c_diff), len(c_diff)), c_diff])


    return sc, he, pl, pl2

# Initialize function (not necessary in this case since we update the plot in the first frame)
def init():
    return sc, he, pl, pl2


frame_rate = 30  # frames per second
duration = 15  # seconds
total_frames = frame_rate * duration
# Create animation


for i in range (1):
    ani = animation.FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True)
    ani2 = animation.FuncAnimation(fig2, update, frames=total_frames, init_func=init, blit=True)
    #ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
    ax2.scatter(resx, resy)
    #ax3.scatter(len(sq_off_rl), np.mean(sq_off))
    plt.show()

# Display animation