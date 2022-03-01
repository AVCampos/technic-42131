# Basic imports
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Port, Direction, Stop, Button, Color
from pybricks.tools import wait

# Initialise the motors
motor_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.B)
motor_function = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
motor_change = Motor(Port.D)

SPEED_CHANGE = 720  # Speed for the function shifting motor


def reset_selector():
    """Moves the function selector to the first position"""

    # Run the motor backwards until it hits the physical limit in the shifting mechanism
    motor_change.run_until_stalled(-SPEED_CHANGE, then=Stop.HOLD)

    # Since the angle that hits the limit is a little over a 90º position of the selector, get the nearest multiple of 90º
    rounded_angle = round(motor_change.angle() / 90, 0) * 90

    # Run the motor to the precise multiple of 90º
    motor_change.run_target(
        speed=SPEED_CHANGE, target_angle=rounded_angle, then=Stop.HOLD, wait=True)


def set_led(angle):
    """Sets the colour of the remote's LED based on the selector's angle"""
    if angle == 0:
        colour = Color.BLUE
    elif angle == 90:
        colour = Color.GREEN
    elif angle == 180:
        colour = Color.YELLOW
    elif angle == 270:
        colour = Color.RED
    else:
        colour = Color.WHITE  # This should never happen, but just in case
    remote.light.on(colour)


# Connect to the remote
remote = Remote(timeout=None)
remote.light.on(Color.WHITE)

# Set the selector to the first position, and mark it as zero
reset_selector()
motor_change.reset_angle(0)
chosen_angle = 0
set_led(chosen_angle)

# Now we can start driving!
while True:
    # Check which buttons are pressed.
    pressed = remote.buttons.pressed()

    # Set the left tread to the left buttons
    speed_left = 0
    if Button.LEFT_PLUS in pressed:
        speed_left += 100
    if Button.LEFT_MINUS in pressed:
        speed_left -= 100

    # Set the right tread to the right buttons
    speed_right = 0
    if Button.RIGHT_PLUS in pressed:
        speed_right += 100
    if Button.RIGHT_MINUS in pressed:
        speed_right -= 100

    # Set the selected function to the red buttons
    speed_function = 0
    if Button.RIGHT in pressed:
        speed_function += 100
    if Button.LEFT in pressed:
        speed_function -= 100

    # Process the green button
    if Button.CENTER in pressed:
        # The mechanism is shifting, let the user know this
        remote.light.on(Color.WHITE)

        chosen_angle += 90  # Move the function selector to the next function

        if chosen_angle > 270:
            # If we're already at the last function and the selector is physically blocked from turning 360º, we need to turn back
            chosen_angle = 0
            reset_selector()  # We can't use run_target() here because it always chooses the shortest path, which would be to turn forward from 270º to 360º instead of back from 270º to 0º
        else:
            # Normal case: just turn the selector to the desired position
            motor_change.run_target(
                speed=SPEED_CHANGE, target_angle=chosen_angle, then=Stop.HOLD, wait=True)

        # The selector is at the desired position; tell the user the good news
        set_led(chosen_angle)

        # Wait for the user to be release the green button
        while Button.CENTER in remote.buttons.pressed():
            wait(10)

    # Apply the selected speed to the thread and function motors
    motor_left.dc(speed_left)
    motor_right.dc(speed_right)
    motor_function.dc(speed_function)

    # Wait
    wait(10)
