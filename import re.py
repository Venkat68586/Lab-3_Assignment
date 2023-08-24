import re

class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

    def __repr__(self):
        return f"Match(location={self.location}, team1={self.team1}, team2={self.team2}, timing={self.timing})"


def get_matches():
    return [
        Match("Mumbai", "India", "Sri Lanka", "DAY"),
        Match("Delhi", "England", "Australia", "DAY-NIGHT"),
        Match("Chennai", "India", "South Africa", "DAY"),
        Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
        Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
        Match("Delhi", "India", "Australia", "DAY"),
    ]


def search_matches(matches, criteria):
    matches_found = []
    for match in matches:
        if criteria == "team":
            if match.team1 == criteria or match.team2 == criteria:
                matches_found.append(match)
        elif criteria == "location":
            if match.location == criteria:
                matches_found.append(match)
        elif criteria == "timing":
            if match.timing == criteria:
                matches_found.append(match)
    return matches_found


def print_matches(matches):
    print("Match Location Team 1 Team 2 Timing")
    for match in matches:
        print(f"{match.location} {match.team1} {match.team2} {match.timing}")


def main():
    matches = get_matches()

    while True:
        print("Select search criteria:")
        print("1. Team")
        print("2. Location")
        print("3. Timing")
        choice = input("Enter your choice: ")

        if choice == "1":
            team = input("Enter team name: ")
            matches_found = search_matches(matches, "team")
        elif choice == "2":
            location = input("Enter location: ")
            matches_found = search_matches(matches, "location")
        elif choice == "3":
            timing = input("Enter timing: ")
            matches_found = search_matches(matches, "timing")
        else:
            print("Invalid choice!")
            continue

        if matches_found:
            print_matches(matches_found)
        else:
            print("No matches found!")

        print("Do you want to continue? (Y/N)")
        choice = input()
        if choice != "Y":
            break


if __name__ == "__main__":
    main()
