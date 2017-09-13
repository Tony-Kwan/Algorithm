class Solution(object):
	def findLongestChain(self, p):
		"""
		:type p: List[List[int]]
		:rtype: int
		"""
		n = len(p)
		r = range(0, n)
		for i in r:
			for j in range(i + 1, n):
				if p[j][0] < p[i][0] or (p[j][0] == p[i][0] and p[j][1] < p[i][1]):
					p[i], p[j] = p[j], p[i]
		dp = [1 for _ in r]
		for i in r:
			for j in range(0, i):
				dp[i] = max(dp[i], dp[j] + 1 if p[i][0] > p[j][1] else dp[j])
		return dp[n - 1]


# print Solution().findLongestChain([[1,1], [1,1]])
# print Solution().findLongestChain([[1,2], [2,3], [3,4]])
# print Solution().findLongestChain([[1,2], [2,3], [3,4], [5,6]])
print Solution().findLongestChain([[-542,150],[-732,980],[-996,9],[523,948],[260,929],[140,856],[-944,360],[-596,-107],[-978,666],[595,829],[540,760],[-964,-540],[409,617],[-757,642],[896,937],[405,795],[848,956],[89,565],[-192,117],[-884,-712],[999,1000],[-392,544],[-777,211],[-438,805],[-376,869],[978,994],[726,995],[-384,246],[284,428],[-815,-311],[992,993],[-764,-557],[814,848],[78,445],[814,908],[-196,-189],[-79,960],[19,531],[807,888],[-634,93],[-871,200],[501,687],[986,987],[-383,465],[-636,286],[-367,668],[33,134],[-249,-127],[-727,812],[-392,642],[-746,72],[-961,564],[843,873],[-833,-132],[-588,-62],[82,430],[-982,838],[-124,175],[-151,327],[-851,4],[-720,468],[-790,443],[309,663],[827,838],[-120,149],[-427,566],[-162,-128],[-231,813],[-41,851],[-425,178],[-442,-296],[475,794],[109,257],[-153,563],[-601,738],[-643,584],[331,590],[-954,587],[627,650],[633,828],[-812,114],[539,887],[296,535],[981,983],[-970,718],[-717,816],[-389,642],[541,916],[410,923],[247,783],[-747,295],[49,660],[243,382],[240,430],[884,901],[-630,-240],[-325,527],[202,571],[161,567],[-77,908],[193,973],[434,568],[600,951],[-688,-418],[-291,392],[891,933],[-913,320],[-588,759],[-794,537],[-495,-304],[-823,-87],[122,459],[225,301],[684,746],[-332,87],[-178,502],[-233,173],[767,947],[513,844],[-679,706],[553,596],[238,781],[63,642],[20,425],[992,995],[688,910],[-589,-378],[613,842],[992,998],[-476,-111],[-572,325],[404,718],[439,804],[457,774],[-327,752],[-457,393],[-636,-381],[858,943],[187,215],[322,716],[-443,-383],[22,785],[-720,-306],[-848,670],[644,736],[-565,604],[-953,-455],[445,831],[-162,841],[165,991],[604,969],[-157,928],[-619,802],[433,868],[-460,-126],[71,475],[-106,343],[-166,859],[-947,197],[335,999],[849,983],[626,804],[58,796],[396,507],[634,666],[-284,854],[-401,981],[161,934],[-219,718],[834,906],[913,922],[-630,207],[-510,-277],[-223,-101],[321,676],[-201,900],[-144,752],[253,417],[330,756],[-619,-278],[-4,360],[403,747],[-136,66],[-112,634],[-718,-282],[779,931],[113,171],[141,353],[-461,957],[-864,112],[-374,228],[-13,429],[-237,102],[272,541],[-376,111],[874,913],[-255,102],[142,437],[701,734],[-193,68],[376,672],[-460,87],[676,856],[-928,554],[23,675],[583,721],[-514,529],[746,887],[-496,141],[-84,799],[416,935],[-421,648],[-341,-140],[328,667],[140,730],[-216,184],[588,897],[-108,567],[199,941],[834,957],[423,488],[-771,939],[250,936],[-93,681],[-214,639],[148,378],[752,763],[854,902],[749,983],[-371,813],[-48,312],[-116,120],[-551,180],[-794,906],[-994,491],[-979,-733],[965,970],[616,835],[540,569],[398,989],[304,885],[-413,-202],[-615,334],[-796,854],[-297,219],[-787,-87],[-577,143],[-273,294],[657,679],[247,393],[-612,980],[975,993],[-519,1000],[459,655],[-879,-16],[-519,-358],[-431,179],[-222,471],[823,839],[652,774],[246,514],[-377,757],[429,545],[-405,752],[986,996],[821,834],[-286,260],[-551,656],[-113,285],[-862,-32],[276,756],[-212,676],[-231,-93],[800,970],[593,630],[-158,170],[168,558],[252,980],[551,703],[358,377],[934,947],[370,912],[-858,-79],[889,903],[-302,479],[-742,453],[-40,33],[790,865],[134,968],[124,450],[-88,694],[-725,482],[-703,-194],[680,773],[75,550],[611,832],[692,991],[356,363],[330,957],[560,604],[-603,-322],[118,285],[-919,977],[-803,772],[458,715],[-790,9],[332,827],[517,724],[898,932],[-920,487],[-604,859],[741,826],[395,478],[317,357],[725,997],[-160,669],[387,442],[174,677],[-747,640],[751,900],[845,870],[710,951],[-682,474],[-785,-784],[373,475],[405,607],[538,897],[761,801],[897,905],[727,945],[-341,-4],[811,878],[467,488],[393,510],[-414,741],[215,605],[378,385],[-400,-225],[760,924],[246,858],[816,868],[237,645],[-677,993],[510,940],[80,903],[-129,275],[-776,194],[-399,974],[779,920],[823,946],[-353,840],[543,942],[214,630],[314,873],[-868,-802],[-27,436],[160,222],[-435,166],[825,945],[79,133],[-91,176],[34,305],[-259,467],[954,983],[312,711],[923,964],[154,402],[414,818],[941,1000],[702,976],[32,584],[-407,1],[-791,292],[-879,525],[-6,530],[617,780],[-42,497],[-29,559],[809,968],[370,599],[-286,432],[-273,373],[-293,966],[-16,688],[-117,666],[617,738],[-136,711],[529,659],[-285,893],[18,243],[-799,707],[733,740],[-494,903],[743,890],[-593,594],[-955,233],[922,967],[359,573],[159,335],[914,922],[-922,-88],[-871,315],[688,740],[-76,857],[473,829],[-366,-213],[-992,744],[-570,855],[615,953],[-57,84],[388,626],[-740,739],[-868,905],[627,639],[247,248],[-97,438],[928,968],[-675,-376],[455,583],[-284,581],[722,879],[-281,148],[850,975],[699,710],[413,498],[-780,815],[-739,-565],[917,935],[-521,-289],[-984,57],[-571,510],[-950,246],[-492,719],[201,590],[-332,-298],[-102,875],[663,914],[-945,-472],[-498,792],[510,831],[220,307],[378,781],[-91,76],[-514,-111],[-375,-318],[-172,556],[-293,310],[633,911],[-25,937],[-440,455],[481,552],[634,713],[-967,-956],[964,970],[-249,220],[-783,-280],[-807,657],[577,790],[-103,252],[-731,197],[-766,900],[672,718],[16,175],[-221,-39],[491,594],[-563,519],[944,964],[503,865],[-549,62],[957,981],[-53,731]])