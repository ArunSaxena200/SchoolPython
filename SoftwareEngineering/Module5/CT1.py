actors = {
    "Citizen": [
        "Report Pothole",
        "View Pothole Status",
        "Report Damage"
    ],
    "Repair Crew": [
        "Update Repair Status",
        "Log Repair Details"
    ],
    "Supervisor": [
        "Assign Repair Crew"
    ],
    "Administrator": [
        "Configure Streets and Districts",
        "Generate Reports"
    ]
}

use_case_descriptions = {
    "Report Pothole": "Submit pothole location, severity, and details",
    "View Pothole Status": "Check the current repair status of a reported pothole",
    "Report Damage": "Submit claims related to vehicle/property damage due to pothole",
    "Assign Repair Crew": "Assign a repair crew to fix a pothole",
    "Update Repair Status": "Update the current repair progress",
    "Log Repair Details": "Log equipment, labor, materials used, and cost",
    "Configure Streets and Districts": "Setup and maintain city mapping data",
    "Generate Reports": "Create reports on pothole statistics and costs"
}

def print_use_cases():
    print("\n=== PHTRS Use Case Summary ===\n")
    for actor, cases in actors.items():
        print(f"\nActor: {actor}")
        for case in cases:
            print(f"  - Use Case: {case}")
            print(f"    Description: {use_case_descriptions[case]}")
    print("\nDiagram should visualize actors on the left/right with use cases in the center.")

if __name__ == "__main__":
    print_use_cases()
