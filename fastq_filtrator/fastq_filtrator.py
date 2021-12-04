# FILTERING FOR GC CONTENT

def gc_filter(input_fastq, gc_bounds, save_filtered):
    if type(gc_bounds) == list or type(gc_bounds) == tuple:
        min_gc = gc_bounds[0]
        max_gc = gc_bounds[1]
    else:
        min_gc = 0
        max_gc = gc_bounds
    lines = []
    good_lines = []
    bad_lines = []
    with open(input_fastq) as file:
        lines = file.readlines()
    i = 1
    if save_filtered is True:
        while i < len(lines) - 4:
            seq = lines[i].upper().strip()
            gc_content = round(((seq.count('C') + seq.count('G'))/len(seq)*100), 1)
            if min_gc <= gc_content <= max_gc:
                good_lines.append(lines[i-1])
                good_lines.append(lines[i])
                good_lines.append(lines[i+1])
                good_lines.append(lines[i+2])
            else:
                bad_lines.append(lines[i-1])
                bad_lines.append(lines[i])
                bad_lines.append(lines[i+1])
                bad_lines.append(lines[i+2])
            i += 4
        return [good_lines, bad_lines]
    else:
        while i < len(lines) - 4:
            seq = lines[i].upper().strip()
            gc_content = round(((seq.count('C') + seq.count('G'))/len(seq)*100), 1)
            if min_gc <= gc_content and gc_content <= max_gc:
                good_lines.append(lines[i-1])
                good_lines.append(lines[i])
                good_lines.append(lines[i+1])
                good_lines.append(lines[i+2])
            i += 4
        return good_lines


# FILTERING FOR LENGTH

def length_filter(good_lines, bad_lines, length_bounds, save_filtered):
    if type(length_bounds) == list or type(length_bounds) == tuple:
        min_len = length_bounds[0]
        max_len = length_bounds[1]
    else:
        min_len = 0
        max_len = length_bounds
    lines = good_lines
    good_lines = []
    i = 1
    if save_filtered is True:
        while i < len(lines) - 4:
            seq = lines[i].upper().strip()
            gc_content = round(((seq.count('C') + seq.count('G'))/len(seq)*100), 1)
            if min_len <= len(seq) <= max_len:
                good_lines.append(lines[i-1])
                good_lines.append(lines[i])
                good_lines.append(lines[i+1])
                good_lines.append(lines[i+2])
            else:
                bad_lines.append(lines[i-1])
                bad_lines.append(lines[i])
                bad_lines.append(lines[i+1])
                bad_lines.append(lines[i+2])
            i += 4
        return [good_lines, bad_lines]
    else:
        while i < len(lines) - 4:
            seq = lines[i].upper().strip()
            gc_content = round(((seq.count('C') + seq.count('G'))/len(seq)*100), 1)
            if min_len <= len(seq) <= max_len:
                good_lines.append(lines[i-1])
                good_lines.append(lines[i])
                good_lines.append(lines[i+1])
                good_lines.append(lines[i+2])
            i += 4
        return good_lines


# FILTERING FOR QUALITY

def quality_filter(good_lines, bad_lines, quality_threshold, save_filtered):
    lines = good_lines
    good_lines = []
    i = 3
    if save_filtered is True:
        while i < len(lines) - 4:
            seq = lines[i].upper().strip()
            quality = 0
            for j in seq:
                quality += (ord(j) - 33)
            mean_quality = quality/len(seq)
            if mean_quality >= quality_threshold:
                good_lines.append(lines[i-3])
                good_lines.append(lines[i-2])
                good_lines.append(lines[i-1])
                good_lines.append(lines[i])
            else:
                bad_lines.append(lines[i-3])
                bad_lines.append(lines[i-2])
                bad_lines.append(lines[i-1])
                bad_lines.append(lines[i])
            i += 4
        return [good_lines, bad_lines]
    else:
        while i < len(lines) - 4:
            seq = lines[i].upper().strip()
            quality = 0
            for j in seq:
                quality += (ord(j) - 33)
            mean_quality = quality/len(seq)
            if mean_quality >= quality_threshold:
                good_lines.append(lines[i-3])
                good_lines.append(lines[i-2])
                good_lines.append(lines[i-1])
                good_lines.append(lines[i])
            i += 4
        return good_lines


# SAVING FILE

def file_maker(good_lines, bad_lines, output_file_prefix, save_filtered):
    with open(output_file_prefix + "_passed.fastq", 'a') as good:
        for line in good_lines:
            good.write(line)
    if save_filtered is True:
        with open(output_file_prefix + "_failed.fastq", 'a') as bad:
            for line in bad_lines:
                bad.write(line)


# THE MAIN FUNCTION

def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False):
    gc = gc_filter(input_fastq, gc_bounds, save_filtered)
    if save_filtered is True:
        good_lines = gc[0]
        bad_lines = gc[1]
        length = length_filter(good_lines, bad_lines, length_bounds, save_filtered)
        new_good_lines = length[0]
        new_bad_lines = length[1]
        Q = quality_filter(new_good_lines, new_bad_lines, quality_threshold, save_filtered)
        good_lines = Q[0]
        bad_lines = Q[1]
        file_maker(good_lines, bad_lines, output_file_prefix, save_filtered)
    else:
        good_lines = gc
        bad_lines = []
        new_good_lines = length_filter(good_lines, bad_lines, length_bounds, save_filtered)
        Q = quality_filter(new_good_lines, bad_lines, quality_threshold, save_filtered)
        file_maker(Q, bad_lines, output_file_prefix, save_filtered)


# RECEIVING ARGUMENTS

print('Welcome to fastq_filtrator!')

input_fastq = input('Enter the path to fastq file: ')

output_file_prefix = input('Enter the prefix for output file(s), without .fastq ')

gc_bounds = (0, 100)
if input('Whould you like to set gc bounds manually ((0, 100) by default), y/n? ') == 'y':
    if input('Whould you like to set minimum gc content? y/n ') == 'y':
        min_gc = int(input('Enter minimum gc content: '))
        max_gc = int(input('Enter maximum gc content: '))
        gc_bounds = (min_gc, max_gc)
    else:
        gc_bounds = int(input('Enter maximum gc content: '))

length_bounds = (0, 2**32)
if input('Whould you like to set length bounds manually ((0, 2**32) by default), y/n? ') == 'y':
    if input('Whould you like to set minimum length? y/n ') == 'y':
        min_len = int(input('Enter minimum length: '))
        max_len = int(input('Enter maximum length: '))
        length_bounds = (min_len, max_len)
    else:
        length_bounds = int(input('Enter maximum length: '))

quality_threshhold = 0
if input('Whould you like to set quality threshold manually (0 by default), y/n? ') == 'y':
    quality_threshold = int(input('Enter quality threshold: '))

save_filtered = False
if input('Whould you like to save the filtered file? y/n ') == 'y':
        save_filtered = True

main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered)
