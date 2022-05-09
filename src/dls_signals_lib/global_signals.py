import signal
from dls_signals_lib.signal import Signal

# Module-based global varible.
# TODO: Change global_signals to a singleton class.
global_sigint = Signal(signal.SIGINT)
