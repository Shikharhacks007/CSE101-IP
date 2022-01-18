import json
import unittest
import a2 as my

# NOTE:
# 1. Make sure your file is named as a2.py and in the same folder as tests.py
# 2. Make sure data.json is also in the same folder as tests.py
# 3. Make sure data.json is the same as the one given in the assignment
#    and no modifications have been done to it


def read_data_from_file(file_path='data.json'):
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


class TestFilterByFirstName(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		first_name = 'Isabella'
		user_output = sorted(my.filter_by_first_name(records, first_name))
		exp_output = [0, 3, 13]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		first_name = 'isabella'
		user_output = sorted(my.filter_by_first_name(records, first_name))
		exp_output = [0, 3, 13]
		self.assertEqual(exp_output, user_output)


	def test_3(self):
		records = read_data_from_file()
		first_name = 'Nonexistent'
		user_output = sorted(my.filter_by_first_name(records, first_name))
		exp_output = []
		self.assertEqual(exp_output, user_output)


class TestFilterByLastName(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		last_name = 'Ramirez'
		user_output = sorted(my.filter_by_last_name(records, last_name))
		exp_output = [0, 58, 95, 121, 186]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		last_name = 'ramirez'
		user_output = sorted(my.filter_by_last_name(records, last_name))
		exp_output = [0, 58, 95, 121, 186]
		self.assertEqual(exp_output, user_output)


	def test_3(self):
		records = read_data_from_file()
		last_name = 'Nonexistent'
		user_output = sorted(my.filter_by_last_name(records, last_name))
		exp_output = []
		self.assertEqual(exp_output, user_output)


class TestFilterByFullName(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		full_name = 'Zoe Smith'
		user_output = sorted(my.filter_by_full_name(records, full_name))
		exp_output = [9, 104]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		full_name = 'Isabella Smith'
		user_output = sorted(my.filter_by_full_name(records, full_name))
		exp_output = [3]
		self.assertEqual(exp_output, user_output)


	def test_3(self):
		records = read_data_from_file()
		full_name = 'isabella smith'
		user_output = sorted(my.filter_by_full_name(records, full_name))
		exp_output = [3]
		self.assertEqual(exp_output, user_output)


	def test_4(self):
		records = read_data_from_file()
		full_name = 'Nonexistent Name'
		user_output = sorted(my.filter_by_full_name(records, full_name))
		exp_output = []
		self.assertEqual(exp_output, user_output)


class TestFilterByAgeRange(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		min_age = 25
		max_age = 30
		user_output = sorted(my.filter_by_age_range(records, min_age, max_age))
		exp_output = [2, 9, 12, 14, 16, 21, 23, 26, 32, 33, 41, 47, 51, 57, 65, 70, 82, 83, 87, 98, 101, 105, 106, 107, 120, 122, 132, 135, 143, 153, 158, 161, 165, 167, 175, 181, 185]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		min_age = 32
		max_age = 32
		user_output = sorted(my.filter_by_age_range(records, min_age, max_age))
		exp_output = [66, 93, 159, 170]
		self.assertEqual(exp_output, user_output)


	def test_3(self):
		records = read_data_from_file()
		min_age = 70
		max_age = 100
		user_output = sorted(my.filter_by_age_range(records, min_age, max_age))
		exp_output = []
		self.assertEqual(exp_output, user_output)


class TestCountByGender(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		user_output = my.count_by_gender(records)
		exp_output = {'male': 97, 'female': 103}
		self.assertEqual(exp_output, user_output)


class TestFilterByAddress(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		address = {'state': 'Delhi'}
		user_output = my.filter_by_address(records, address)
		exp_output = [
			{'first_name': 'Samarth',  'last_name': 'Nelson'},
			{'first_name': 'Azad',     'last_name': 'Davis'},
			{'first_name': 'Ishaan',   'last_name': 'Johnson'},
			{'first_name': 'Savannah', 'last_name': 'King'},
			{'first_name': 'Harshil',  'last_name': 'Johnson'},
			{'first_name': 'Jeet',     'last_name': 'Hernandez'}
		]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		address = {'state': 'delhi'}
		user_output = my.filter_by_address(records, address)
		exp_output = [
			{'first_name': 'Samarth',  'last_name': 'Nelson'},
			{'first_name': 'Azad',     'last_name': 'Davis'},
			{'first_name': 'Ishaan',   'last_name': 'Johnson'},
			{'first_name': 'Savannah', 'last_name': 'King'},
			{'first_name': 'Harshil',  'last_name': 'Johnson'},
			{'first_name': 'Jeet',     'last_name': 'Hernandez'}
		]
		self.assertEqual(exp_output, user_output)


	def test_3(self):
		records = read_data_from_file()
		address = {
			'house_no': 513,
            'block': 'E',
            'town': 'Gokal Pur',
            'city': 'Siri',
            'state': 'Delhi',
            'pincode': 110011
		}
		user_output = my.filter_by_address(records, address)
		exp_output = [
			{'first_name': 'Ishaan', 'last_name': 'Johnson'}
		]
		self.assertEqual(exp_output, user_output)


class TestFindAlumni(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		institute_name = 'QNERCSS'
		user_output = my.find_alumni(records, institute_name)
		exp_output = [
			{'first_name': 'Rushil',    'last_name': 'Mitchell', 'percentage': 45.03697},
			{'first_name': 'Wriddhish', 'last_name': 'Gonzalez', 'percentage': 49.18812},
			{'first_name': 'Aryan',     'last_name': 'Davis',    'percentage': 93.95699},
			{'first_name': 'Scarlett',  'last_name': 'Rivera',   'percentage': 48.15452},
			{'first_name': 'Bella',     'last_name': 'Perez',    'percentage': 60.31215},
			{'first_name': 'Sofia',     'last_name': 'Williams', 'percentage': 87.71204},
			{'first_name': 'Dev',       'last_name': 'Adams',    'percentage': 89.48979},
			{'first_name': 'Anna',      'last_name': 'Taylor',   'percentage': 47.94899},
			{'first_name': 'Paisley',   'last_name': 'Allen',    'percentage': 60.54851}
		]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		institute_name = 'Nonexistent'
		user_output = my.find_alumni(records, institute_name)
		exp_output = []
		self.assertEqual(exp_output, user_output)


class TestFindTopperOfEachInstitute(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		user_output = my.find_topper_of_each_institute(records)
		exp_output = {
			'TKRYTU': 155,
			'LLDVY': 50,
			'KVGLHL': 7,
			'JWBTYC': 48,
			'MAQZIES': 102,
			'APTASAJ': 190,
			'QNERCSS': 15,
			'EMCUYFH': 117,
			'GSMJS': 7,
			'NXTECJC': 164,
			'SYLUH': 11,
			'AKUZM': 107,
			'KFBQTR': 15,
			'EBUNL': 117,
			'WGRCR': 59
		}
		self.assertEqual(exp_output, user_output)


class TestFindBloodDonors(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		receiver_person_id = 10
		user_output = my.find_blood_donors(records, receiver_person_id)
		for pid in user_output:
			user_output[pid].sort()

		exp_output = {
			1: ['753617018'],
			4: ['768860400'],
			6: ['683611689'],
			7: ['406086149', '659619250'],
			8: ['791173268'],
			11: ['452364836'],
			13: ['478254867'],
			15: ['430967626', '814549547'],
			16: ['110662594', '150147063'],
			20: ['287867596', '945753543'],
			21: ['359153438'],
			22: ['850348593', '898824611'],
			24: ['322040466', '432558801'],
			26: ['696893905', '820878603'],
			29: ['231728477', '444427857'],
			32: ['923819092'],
			34: ['328324572', '683692230'],
			35: ['366336764', '950441309'],
			36: ['183855302', '988262711'],
			41: ['706709510'],
			42: ['444832838'],
			43: ['616187098'],
			44: ['100054552', '716516117'],
			46: ['757948643', '847802764'],
			48: ['999619254'],
			51: ['688685508'],
			52: ['419470243'],
			53: ['757002219', '877109025'],
			54: ['335019731', '884610891'],
			55: ['319481887', '448149554'],
			56: ['698061592', '745089427'],
			57: ['743290236'],
			60: ['560103185'],
			64: ['648960810'],
			66: ['782275738'],
			67: ['733407404'],
			68: ['122952730', '339571902'],
			71: ['165744475', '905108690'],
			72: ['417923157', '464267551'],
			74: ['842399789'],
			77: ['748641603'],
			78: ['434401315', '630521156'],
			82: ['479819111', '624429381'],
			83: ['589393713'],
			84: ['892336601'],
			86: ['346634787'],
			87: ['353966953', '802295875'],
			90: ['207836307'],
			93: ['150525699', '933339748'],
			94: ['685443259', '732192114'],
			95: ['672849960'],
			96: ['516826150', '976618541'],
			99: ['435461294', '673087102'],
			100: ['122596366', '967849065'],
			103: ['110283462', '206507883'],
			104: ['524006600'],
			107: ['224621170', '226443626'],
			108: ['539080197'],
			109: ['654685276'],
			111: ['431267435', '979533367'],
			113: ['465810302', '969401965'],
			114: ['506770918', '682746782'],
			119: ['524479212'],
			120: ['281177485', '975565203'],
			122: ['389816299', '559521370'],
			123: ['373799580', '541025691'],
			125: ['318256026', '882044482'],
			126: ['804191450'],
			130: ['249782763'],
			133: ['681364063', '993967497'],
			134: ['474384857', '537485085'],
			135: ['740554285'],
			136: ['377574896'],
			138: ['240465416'],
			141: ['756955541'],
			142: ['311311639', '952391982'],
			151: ['775572575', '838524761'],
			154: ['645244322'],
			159: ['960371763'],
			163: ['234476874', '605331918'],
			166: ['293162976'],
			169: ['482361094'],
			173: ['883401535'],
			174: ['973488646'],
			177: ['450649880', '587019129'],
			179: ['188396729', '997112739'],
			180: ['323154274', '639564350'],
			185: ['267033439', '847498551'],
			186: ['150320749', '984989731'],
			187: ['408230520', '760697675'],
			191: ['107288425'],
			192: ['214198336'],
			193: ['330430344'],
			196: ['120239332'],
			199: ['338049626', '996225342']
		}
		self.assertEqual(exp_output, user_output)


class TestGetCommonFriends(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		list_of_ids = [1, 13]
		user_output = sorted(my.get_common_friends(records, list_of_ids))
		exp_output = [114, 174]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		list_of_ids = [2, 15, 109, 125]
		user_output = sorted(my.get_common_friends(records, list_of_ids))
		exp_output = [143]
		self.assertEqual(exp_output, user_output)


	def test_3(self):
		records = read_data_from_file()
		list_of_ids = [4, 8]
		user_output = sorted(my.get_common_friends(records, list_of_ids))
		exp_output = []
		self.assertEqual(exp_output, user_output)


class TestIsRelated(unittest.TestCase):
	def test_1(self):
		records = read_data_from_file()
		person_id_1 = 0
		person_id_2 = 106
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = True # 0 -> 106
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = read_data_from_file()
		person_id_1 = 0
		person_id_2 = 7
		user_output = my.is_related(records, person_id_1, person_id_2)
		exp_output = True # 0 -> 33 -> 76 -> 20 -> 19 -> 7
		self.assertEqual(exp_output, user_output)


class TestDeleteById(unittest.TestCase):
	def test_1(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]
		
		person_id = 56
		user_output = my.delete_by_id(records, person_id)

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]
		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
		]

		person_id = 1
		user_output = my.delete_by_id(records, person_id)

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]
		
		self.assertEqual(exp_output, user_output)


class TestAddFriend(unittest.TestCase):
	def test_1(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		person_id = 0
		friend_id = 2
		user_output = my.add_friend(records, person_id, friend_id)
		user_output[person_id]['friend_ids'].sort()
		user_output[friend_id]['friend_ids'].sort()

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
					2
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
					0
				]
			},
		]

		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
					2
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
					0
				]
			},
		]

		person_id = 0
		friend_id = 2
		user_output = my.add_friend(records, person_id, friend_id)
		user_output[person_id]['friend_ids'].sort()
		user_output[friend_id]['friend_ids'].sort()

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
					2
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
					0
				]
			},
		]

		self.assertEqual(exp_output, user_output)


class TestRemoveFriend(unittest.TestCase):
	def test_1(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
					2
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
					0
				]
			},
		]

		person_id = 0
		friend_id = 2
		user_output = my.remove_friend(records, person_id, friend_id)
		user_output[person_id]['friend_ids'].sort()
		user_output[friend_id]['friend_ids'].sort()

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		person_id = 0
		friend_id = 2
		user_output = my.remove_friend(records, person_id, friend_id)
		user_output[person_id]['friend_ids'].sort()
		user_output[friend_id]['friend_ids'].sort()

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		self.assertEqual(exp_output, user_output)


class TestAddEducation(unittest.TestCase):
	def test_1(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]
		
		person_id = 1
		user_output = my.add_education(records, person_id, 'NEWEDU', False, 54.321)
		
		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					},
					{
						'institute': 'NEWEDU',
						'ongoing': False,
						'percentage': 54.321
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		self.assertEqual(exp_output, user_output)


	def test_2(self):
		records = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					}
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		person_id = 1
		user_output = my.add_education(records, person_id, 'NEWEDU', True, 0)

		exp_output = [
			{
				'id': 0,
				'first_name': 'Imaran',
				'last_name': 'Hill',
				'age': 28,
				'gender': 'male',
				'address': {
					'house_no': 544,
					'block': 'O',
					'town': 'Narela',
					'city': 'Lal Kot',
					'state': 'Haryana',
					'pincode': 110013
				},
				'education': [
					{
						'institute': 'NXTECJC',
						'ongoing': True
					},
					{
						'institute': 'AKUZM',
						'ongoing': True
					}
				],
				'blood_group': 'O',
				'contacts': [
					'150147063',
					'110662594'
				],
				'friend_ids': [
					1,
				]
			},
			{
				'id': 1,
				'first_name': 'Piper',
				'last_name': 'Flores',
				'age': 23,
				'gender': 'female',
				'address': {
					'house_no': 251,
					'block': 'ELX',
					'town': 'Taj Pul',
					'city': 'Tughlakabad',
					'state': 'Tripura',
					'pincode': 110007
				},
				'education': [
					{
						'institute': 'TKRYTU',
						'ongoing': False,
						'percentage': 68.87386
					},
					{
						'institute': 'EBUNL',
						'ongoing': True
					},
					{
						'institute': 'GSMJS',
						'ongoing': True
					},
					{
						'institute': 'NEWEDU',
						'ongoing': True,
					},
				],
				'blood_group': 'B',
				'contacts': [
					'971036052'
				],
				'friend_ids': [
					0
				]
			},
			{
				'id': 2,
				'first_name': 'Harper',
				'last_name': 'Adams',
				'age': 22,
				'gender': 'female',
				'address': {
					'house_no': 758,
					'block': 'GUR',
					'town': 'Jaffrabad',
					'city': 'Firozabad',
					'state': 'Lakshadweep',
					'pincode': 110009
				},
				'education': [],
				'blood_group': 'O',
				'contacts': [
					'850348593',
					'898824611'
				],
				'friend_ids': [
				]
			},
		]

		self.assertEqual(exp_output, user_output)


if __name__ == '__main__':
	unittest.main()
