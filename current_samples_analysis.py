def find_range_count(current_samples):
    temp=set(current_samples)
    sample_range_count=set()
    for i in current_samples:
        range_length=0
        if i-1 not in temp:
            sample_count=0
            start_of_range=i
            while (i+range_length in current_samples):
                sample_count+=current_samples.count(i+range_length)
                range_length+=1
            end_of_range=i+range_length
        sample_range_count.add((start_of_range,end_of_range-1,sample_count))
    return sample_range_count

def csv_formatter(input_data):
    csv_format = str((str(input_data[0])+"-"+str(input_data[1])+", "+str(input_data[2])))
    return csv_format

def print_on_console(message):
    print(message)
