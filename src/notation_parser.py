# A parser to convert algebraic notation into dict e4 -> {"isValid": true}
from typing import Optional, Union, Dict
import re

Piece = Union["pawn", "king", "queen", "knight", "rook", "bishop"]

if __name__ == "__main__":
  pass

class ParseResponse:
  def __init__(self):
    self.isValid: bool = False
    self.input: str = ""
    self.piece: Optional[Piece] = None
    self.from_: Optional[str] = None
    self.fromFile: Optional[str] = None
    self.fromRank: Optional[str] = None
    self.to: Optional[str] = None
    self.toFile: Optional[str] = None
    self.toRank: Optional[str] = None
    self.isCapture: bool = False
    self.isCheck: bool = False
    self.isCheckmate: bool = False
    self.isCastle: bool = False
    self.isPromoted: bool = False
    self.promotePiece: Optional[Piece] = None
    self.castleSide: Optional[str] = None
    
  
  def __repr__(self):
    return (
      f"ParseResponse(isValid={self.isValid}, input='{self.input}', "
      f"piece={self.piece}, from_={self.from_}, fromFile={self.fromFile}, "
      f"fromRank={self.fromRank}, to={self.to}, toFile={self.toFile}, "
      f"toRank={self.toRank}, isCapture={self.isCapture}, isCheck={self.isCheck}, "
      f"isCheckmate={self.isCheckmate}, isCastle={self.isCastle}, "
      f"isPromoted={self.isPromoted}, promotePiece={self.promotePiece}, "
      f"castleSide={self.castleSide})"
    )

# parser("bxc8=N")
def parser(str_: str) -> ParseResponse:
  obj = ParseResponse()
  obj.input = str_
  
  if not isinstance(str_, str) or str_ == "":
    return obj
  if len(str_) < 2 or len(str_) > 8:
    return obj

  validChar = "x+#=KQBNRPabcdefgh12345678O-"

  if not all(char in validChar for char in str_):
    return obj

  if "+" in str_:
    if str_[-1] != "+":
      return obj
    obj.isCheck = True
    str_ = str_.replace("+", "")

  if "#" in str_:
    if str_[-1] != "#":
      return obj
    obj.isCheckmate = True
    str_ = str_.replace("#", "")

  if "x" in str_:
    if not (str_[1] == "x" or str_[2] == "x"):
      return obj
    obj.isCapture = True
    str_ = str_.replace("x", "")

  if "=" in str_:
    if str_[-2:] != "=":
      return obj
    promoted = str_[-1]
    if not (promoted in "QKNRBP" and promoted != "K"):
      return obj
    obj.isPromoted = True
    obj.promotePiece = expand_piece_abbr(promoted)
    str_ = str_.split("=")[0]

  if str_ == "O-O":
    obj.isValid = True
    obj.isCastle = True
    obj.castleSide = "short"
    return obj

  if str_ == "O-O-O":
    obj.isValid = True
    obj.isCastle = True
    obj.castleSide = "long"
    return obj

  if len(str_) == 2:
    if not is_valid_location(str_):
      return obj
    obj.isValid = True
    obj.piece = "pawn"
    obj.to = str_
    obj.toFile, obj.toRank = parse_place(obj.to)
    return obj

  is_pawn = any(char.isalpha() and char.islower() for char in str_)
  if is_pawn:
    obj.isValid = True
    obj.piece = "pawn"
    obj.to = str_[-2:]
    obj.toFile, obj.toRank = parse_place(obj.to)
    obj.from_ = str_[0]
    obj.fromFile, obj.fromRank = parse_place(obj.from_)
    return obj

  is_valid_power_piece = str_[0] in "QKNRBP"
  if not is_valid_power_piece:
    return obj

  obj.piece = expand_piece_abbr(str_[0])
  obj.to = str_[-2:]
  obj.toFile, obj.toRank = parse_place(obj.to)

  if len(str_) == 3:
    obj.isValid = True
    return obj

  if not (obj.piece == "rook" or obj.piece == "knight"):
    return obj

  obj.from_ = str_[1]
  obj.fromFile, obj.fromRank = parse_place(obj.from_)
  obj.isValid = True

  return obj

def is_valid_location(str_: str) -> bool:
  return bool(re.match("[a-h][1-8]", str_))

def parse_place(loc: str) -> Dict[str, Optional[str]]:
  if not loc:
    return {"file": None, "rank": None}
  if len(loc) == 2:
    return {"file": loc[0], "rank": loc[1]}
  if any(char.isalpha() for char in loc):
    return {"file": loc, "rank": None}
  if any(char.isdigit() for char in loc):
    return {"file": None, "rank": loc}
  return {"file": None, "rank": None}

def expand_piece_abbr(char: str) -> Optional[Piece]:
  pieces = {"Q": "queen", "K": "king", "N": "knight", "R": "rook", "B": "bishop", "P": "pawn"}
  return pieces.get(char, None)
