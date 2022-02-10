# example: 123 | 12.3 | -123 |.3 | 1.5e5

from enum import Enum

class DigitState(Enum):
    BEGIN =0
    NEGATIVE1 = 1
    DIGIT1 = 2
    DOT =3
    DIGIT2=4
    E=5
    NEGATIVE2 = 6
    DIGIT3=7

next_state = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.DIGIT2 :[DigitState.DIGIT2,DigitState.E],
    DigitState.E: [DigitState.NEGATIVE2,DigitState.DIGIT3],
    DigitState.NEGATIVE2 :[DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3]
}

digit_lambdas = {
    DigitState.BEGIN: lambda x:True,
    DigitState.NEGATIVE1: lambda x:x=='-',
    DigitState.DIGIT1: lambda x: x.isdigit(),
    DigitState.DOT: lambda x:x=='.',
    DigitState.DIGIT2 :lambda x: x.isdigit(),
    DigitState.E: lambda x: x =='e',
    DigitState.NEGATIVE2 :lambda x:x=='-',
    DigitState.DIGIT3: lambda x: x.isdigit()
}

def is_number(s:str)-> bool:
    state = DigitState.BEGIN
    for ch in s:
        found_next_state = False
        for next in next_state[state]:
            if digit_lambdas[next](ch):
                state = next
                found_next_state = True
                break
        if not found_next_state:
            return False

    return state in (DigitState.DIGIT1,DigitState.DIGIT2,DigitState.DIGIT3)

print(is_number("-12.3"))

