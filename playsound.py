import logging
logger=logging.getLogger(__name__)
_openedSoundsWin = []

class PlaysoundException(Exception):
    pass

def _canonicalizePath(path):
    import sys
    if sys.version_info[0] >= 3:
        return str(path)
    else:
        return path

def playsound(sound, block = True):
    sound = f"\"{_canonicalizePath(sound)}\""

    from ctypes import create_unicode_buffer, windll, wintypes
    windll.winmm.mciSendStringW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.UINT, wintypes.HANDLE]
    windll.winmm.mciGetErrorStringW.argtypes = [wintypes.DWORD, wintypes.LPWSTR, wintypes.UINT]

    def winCommand(command):
        bufLen = 600
        buf = create_unicode_buffer(bufLen)
        errorCode = int(windll.winmm.mciSendStringW(command, buf, bufLen - 1, 0))  # use widestring version of the function
        if errorCode:
            errorBuffer = create_unicode_buffer(bufLen)
            windll.winmm.mciGetErrorStringW(errorCode, errorBuffer, bufLen - 1)  # use widestring version of the function
            exceptionMessage = (f'\n    Error {str(errorCode)} for command:'
                                f'\n    {command}' +
                                f'\n    {errorBuffer.value}')
            raise PlaysoundException(exceptionMessage)

    logger.debug('Starting')
    if sound in _openedSoundsWin:
        try:
            winCommand(u'close {}'.format(sound))
        except PlaysoundException:
            logger.debug(u'Failed to close the file before open: {}'.format(sound))

    try:
        winCommand(u'open {}'.format(sound))
    except PlaysoundException as e:
        logger.error(e)
        raise e
    _openedSoundsWin.append(sound)

    try:
        winCommand(u'play {}{}'.format(sound, ' wait' if block else ''))
        logger.debug('Returning')
    except PlaysoundException as e:
        logger.error(e)
        try:
            winCommand(u'close {}'.format(sound))
        except PlaysoundException:
            logger.warning(u'Failed to close the file after play: {}'.format(sound))
        raise e
    finally:
        if block:
            try:
                winCommand(u'close {}'.format(sound))
            except PlaysoundException:
                logger.warning(u'Failed to close the file after play: {}'.format(sound))