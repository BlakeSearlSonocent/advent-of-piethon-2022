from pie.file_utils import file_to_string_list
from pie.list_utils import windowed


def first_packet_marker_index(subroutine_size: int):
    datastream = list(file_to_string_list("six/input.txt")[0])
    subroutines = windowed(datastream, subroutine_size)

    for idx, subroutine in enumerate(subroutines):
        if len(set(subroutine)) == subroutine_size:
            print(idx + subroutine_size)
            break


if __name__ == "__main__":
    first_packet_marker_index(4)
    first_packet_marker_index(14)
