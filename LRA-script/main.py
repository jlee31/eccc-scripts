import os 

class Record:
    def __init__(self, name, asset_id, reference_id, location, sublocation, additional_info=None):
        self.name = name
        self.asset_id = asset_id
        self.reference_id = reference_id
        self.location = location
        self.sublocation = sublocation
        self.additional_info = additional_info

    def get_display_text(self):
        lines = [
            f"Name: {self.name}",
            f"Asset ID: {self.asset_id}",
            f"Reference ID: {self.reference_id}",
            f"Location: {self.location}",
            f"Sublocation: {self.sublocation}"
        ]
        if self.additional_info:
            lines.append(f"Additional Info: {self.additional_info}")
        lines.append("")  # Add a blank line for spacing
        return "\n".join(lines)

def is_yes(answer):
    return answer.strip().lower() in ['y', 'yes', 'yeah', 'ye']

def is_no(answer):
    return answer.strip().lower() in ['n', 'no', 'nah', 'nope']

def get_record_input():
    name = input("Enter name: ")
    asset_id = input("Enter asset ID: ")
    reference_id = input("Enter reference ID: ")
    location = input("Enter location: ")
    sublocation = input("Enter sublocation: ")
    
    answer = input("Include additional information? (yes/no): ")
    needs_additional = is_yes(answer)
    additional_info = input("Enter additional info: ") if needs_additional else None
    
    return Record(name, asset_id, reference_id, location, sublocation, additional_info)

def main():
    records = []
    ongoing = True
    
    output_file = "output.txt"

    print("RECORD COLLECTION TOOL")

    while ongoing:
        answer = input("Do you want to add a record? (yes/no): ")

        if is_yes(answer):        
            records.append(get_record_input())

        elif is_no(answer):
            ongoing = False

            with open(output_file, "w") as file:
                file.write("COLLECTED RECORDS\n")
                file.write("=" * 79 + "\n")
                for record in records:
                    file.write(record.get_display_text())

            print(f"\nRecords saved to {output_file}")
            os.startfile(output_file)  # Opens the file after it's created

if __name__ == "__main__":
    main()