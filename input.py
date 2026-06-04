import msvcrt

def get_key():
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
            return {b'H': 'UP', b'P': 'DOWN', b'K': 'LEFT', b'M': 'RIGHT'}.get(key)
        if key == b'q':
            return 'QUIT'
        if key in (b's', b'S'):
            return 'RESTART'
    return None
