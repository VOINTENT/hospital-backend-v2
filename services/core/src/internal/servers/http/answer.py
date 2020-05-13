def get_response(status: int or None = None, msg: str or None = None, data: dict or list = None) -> dict:
    return {
        'status': status,
        'msg': msg,
        'data': data
    }


def get_response_with_validation_mistakes(mistakes: dict):
    mistake = list(mistakes.items())[0][1]
    if len(mistake) > 0 and mistake[0] > 1:
        return get_response(status=mistake[0], msg=mistake[1])

    return get_response()
