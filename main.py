import numpy as np
import matplotlib.pyplot as plt

def wiener_process(t):
    """
    Generate a 1D Wiener process.

    Parameters:
    - num_steps: Number of steps in the process.
    - dt: Time step size.

    Returns:
    - A NumPy array representing the Wiener process.
    """
    dt = np.diff(t)
    increments = np.sqrt(dt) * np.random.normal(size=len(dt))

    # # Cumulative sum to obtain the Wiener process
    wiener_process = np.cumsum(increments)

    # # Prepend 0 to make the process start at 0
    wiener_process = np.insert(wiener_process, 0, 0.0)

    return wiener_process


def plot_random_wiener(n):
    for _ in range(n):
        timesteps = np.arange(0, 100, 0.1)
        wiener = wiener_process(timesteps)
        plt.plot(timesteps, wiener, color='w', linewidth=0.1)
        ax = plt.gca()
        ax.set_facecolor('black')


if __name__ == '__main__':
    # Example usage
    # num_steps = 1000
    # Plot the Wiener process
    plot_random_wiener(1000)

    plt.title('1D Wiener Process')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()
