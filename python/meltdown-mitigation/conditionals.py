"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    # Establish threshold constants
    TEMPERATURE_THRESHOLD = 800
    NEUTRON_THRESHOLD = 500
    PRODUCT_THRESHOLD = 500000

    # Determine product
    product = temperature * neutrons_emitted

    if (temperature < TEMPERATURE_THRESHOLD 
        and neutrons_emitted > NEUTRON_THRESHOLD 
        and product < PRODUCT_THRESHOLD):
        return True
    else: 
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    # Establish threshold constants
    GREEN_THRESHOLD = 80
    ORANGE_THRESHOLD = 60
    RED_THRESHOLD = 30

    # Calculate current power and efficiency of reactor
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= GREEN_THRESHOLD:
        return 'green'
    elif efficiency >= ORANGE_THRESHOLD:
        return 'orange'
    elif efficiency >= RED_THRESHOLD:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    # Establish threshold constants
    LOW_THRESHOLD = threshold * .90
    NORMAL_THRESHOLD_TOP = threshold + (threshold * .10)
    NORMAL_THRESHOLD_BOTTOM = threshold - (threshold * .10)

    # Calculate status
    status = temperature * neutrons_produced_per_second

    if status < LOW_THRESHOLD:
        return 'LOW'
    elif NORMAL_THRESHOLD_BOTTOM < status < NORMAL_THRESHOLD_TOP:
        return 'NORMAL'
    else:
        return 'DANGER'