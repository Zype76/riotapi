from RiotAPI import RiotAPI

def main():
	api = RiotAPI('redacted')
	r = api.get_summoner_by_name('Zype76')
	print r

	
if __name__ == "__main__":
	main()