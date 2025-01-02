# Initial packets in the bucket
storage = 0

# Total number of times bucket content is checked
no_of_queries = 4

# Total number of packets that can be accommodated in the bucket
bucket_size = 10

# Number of packets that enters the bucket at a time
input_pkt_size = 4

# Number of packets that exits the bucket at a time
output_pkt_size = 1

for i in range(0, no_of_queries):  # space left
    size_left = bucket_size - storage
    if input_pkt_size <= size_left:
        # Update storage
        storage += input_pkt_size
    else:
        print("Packet loss =", input_pkt_size)

    print(f"Buffer size = {storage} out of bucket size = {bucket_size}")

    # As packets are sent out into the network, the size of the storage decreases
    storage -= output_pkt_size
