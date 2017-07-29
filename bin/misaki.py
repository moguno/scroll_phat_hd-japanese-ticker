import struct
import string
import io
import os

# FONTX2形式のビットマップをScroll pHAT HD形式に変換する
def fontx_to_scrollphathd(fontx):
	result = [None] * 7

	for line in range(7):
		target = [0x00] * 8
		result[line] = target 

		for bit in range(8):
			if ((fontx[line] >> bit) & 0x01) != 0x00:
				target[7 - bit] = 0xff

	return result
	
# 美咲フォント（FONTX2形式全角）を開く
file = open(os.path.dirname(__file__) + "/MISAKI.FNT", "rb")
data = file.read()
file.close()

fp = io.BytesIO(data)

header = struct.unpack("6s8sBBBB", fp.read(18))

block_cnt = header[5]

code_ranges = struct.iter_unpack("HH", fp.read(4 * block_cnt))

data = {}

for code_range in code_ranges:
	cnt = code_range[1] - code_range[0] + 1
	bitmaps = struct.iter_unpack("8B", fp.read(8 * cnt))

	for (i, bitmap) in enumerate(bitmaps):
		try:
			code = code_range[0] + i

			# ユニコードのコードポイントを得る
			unicode_code = ord(struct.unpack("2s", struct.pack(">H", code))[0].decode("sjis"))

			data[unicode_code] = fontx_to_scrollphathd(bitmap)

		except UnicodeDecodeError:
			pass

fp.close()

# 半角文字は全角用のビットマップで表示することとする。

# 数字
for char in string.digits:
	code = ord(char)
	data[code] = data[0xff10 + (code - ord(string.digits[0]))]

# 小文字
for char in string.ascii_lowercase:
	code = ord(char)
	data[code] = data[0xff41 + (code - ord(string.ascii_lowercase[0]))]

# 大文字
for char in string.ascii_uppercase:
	code = ord(char)
	data[code] = data[0xff21 + (code - ord(string.ascii_uppercase[0]))]

# 記号
data[ord(" ")] = data[ord("　")]
data[ord("!")] = data[ord("！")]
data[ord("\"")] = data[ord("”")]
data[ord("#")] = data[ord("＃")]
data[ord("$")] = data[ord("＄")]
data[ord("%")] = data[ord("％")]
data[ord("&")] = data[ord("＆")]
data[ord("'")] = data[ord("’")]
data[ord("(")] = data[ord("（")]
data[ord(")")] = data[ord("）")]
data[ord("*")] = data[ord("＊")]
data[ord("+")] = data[ord("＋")]
data[ord(",")] = data[ord("，")]
data[ord("-")] = data[ord("−")]
data[ord("/")] = data[ord("／")]
data[ord(":")] = data[ord("：")]
data[ord(";")] = data[ord("；")]
data[ord("<")] = data[ord("＜")]
data[ord("=")] = data[ord("＝")]
data[ord(">")] = data[ord("＞")]
data[ord("?")] = data[ord("？")]
data[ord("@")] = data[ord("＠")]
data[ord("[")] = data[ord("［")]
data[ord("\\")] = data[ord("＼")]
data[ord("]")] = data[ord("］")]
data[ord("^")] = data[ord("＾")]
data[ord("_")] = data[ord("＿")]
data[ord("`")] = data[ord("｀")]
data[ord("{")] = data[ord("｛")]
data[ord("|")] = data[ord("｜")]
data[ord("}")] = data[ord("｝")]
data[ord("~")] = data[ord("〜")]
data[ord(".")] = data[ord("．")]
data[ord(",")] = data[ord("，")]

height = 7
width = 8
