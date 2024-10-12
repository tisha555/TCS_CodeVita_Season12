import sys
import bisect

def main():
    # Read input
    input_lines = sys.stdin.read().split('\n')
    if len(input_lines) < 2:
        good_string = input_lines[0].strip()
        student_name = ''
    else:
        good_string = input_lines[0].strip()
        student_name = input_lines[1].strip()

    # Preprocess good string
    good_characters = set(good_string)
    sorted_ascii_values = sorted(set(ord(c) for c in good_string))
    
    # Initialize previous good character
    if not good_string:
        # Edge case: empty good string, but as per constraints, len(good string)>=1
        print(0)
        sys.exit()
    previous_ascii = ord(good_string[0])

    total_distance = 0

    for char in student_name:
        if char in good_characters:
            # No distance added, update previous good character
            previous_ascii = ord(char)
            continue

        target_ascii = ord(char)
        position = bisect.bisect_left(sorted_ascii_values, target_ascii)

        if position == 0:
            selected_ascii = sorted_ascii_values[0]
            distance = abs(target_ascii - selected_ascii)
        elif position == len(sorted_ascii_values):
            selected_ascii = sorted_ascii_values[-1]
            distance = abs(target_ascii - selected_ascii)
        else:
            left_ascii = sorted_ascii_values[position - 1]
            right_ascii = sorted_ascii_values[position]
            left_distance = abs(left_ascii - target_ascii)
            right_distance = abs(right_ascii - target_ascii)

            if left_distance < right_distance:
                selected_ascii = left_ascii
                distance = left_distance
            elif right_distance < left_distance:
                selected_ascii = right_ascii
                distance = right_distance
            else:
                # Tie: choose the one closest to previous good character
                if abs(previous_ascii - left_ascii) < abs(previous_ascii - right_ascii):
                    selected_ascii = left_ascii
                else:
                    selected_ascii = right_ascii
                distance = abs(previous_ascii - selected_ascii)
        
        # Add distance to total
        total_distance += distance
        # Update previous good character
        previous_ascii = selected_ascii

    # Output the total distance
    print(total_distance, end='')

if __name__ == "__main__":
    main()
