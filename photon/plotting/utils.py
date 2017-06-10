import math

__all__ = ['description', 'sci_formatter', 'pad_range']


def description(fig, ext_label, x=0.89, start=0.96, deltay=0.03, **kwargs):
    """
    Given an array of strings add them to a plot one per line at the specified position

    :param fig: Figure to add the description to
    :param ext_label: The array of strings
    :param x: Horizontal position
    :param start: Vertical position of the first line
    :param deltay: Separation between lines
    :param kwargs: Keyword arguments for figure.text
    """
    if ext_label is not None:
        y = start
        for line in ext_label:
            fig.text(x, y, line, kwargs)
            y -= deltay


def sci_formatter(x, p):
    """
    Format the tick label in scientific notation with one decimal figure

    :type p: object
    :param x: Value to be formatted
    :param p: Position
    :return: Formatted string
    """
    if x == 0:
        return "0"
    else:
        xpow = math.floor(math.log10(x))
        val = x / (10 ** xpow)
        return "%.1fE%d" % (val, xpow)


def pad_range(max_val):
    """
    Pad the maximum range for a distribution so that the biggest bar
    in the histogram is not too close to the edge of the plot

    :param max_val: The maximum value in the histogram
    :return: The maximum range to use for the plot
    """
    cur_pow = 10 ** math.floor(math.log10(max_val))
    val = math.ceil(max_val / cur_pow)
    max_range = val * cur_pow
    # Make sure the max_range is at least 10% larger than the unit
    if max_range - max_val < cur_pow * 0.1:
        max_range = (val + 1) * cur_pow
    print ("Max value={} max range={}".format(max_val, max_range))
    return max_range
