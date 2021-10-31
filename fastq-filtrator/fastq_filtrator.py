# Filtering based on GC-content and filtering based on length

def len_and_gc(file, length_bounds, gc_bounds, save_filtered, good_lines, bad_lines):
    with open(file) as file:
        count = 2  
        number = 0  
        for line in file:
            count += 1
            n += 1
            if count == 4:
                count = 0
                sequence = line.upper().strip()
                gc_content = round(((sequence.count('C') + sequence.count('G'))/len(sequence)*100), 1)  # counting gc-content
                if length_bounds[0] <= len(sequence) <= length_bounds[1] and gc_bounds[0] <= gc_content <= gc_bounds[1]:
                    good_lines.add(n - 1)
                    good_lines.add(n)
                    good_lines.add(n + 1)
                    good_lines.add(n + 2)
                elif save_filtered is True:
                    bad_lines.add(n - 1)
                    bad_lines.add(n)
                    bad_lines.add(n + 1)
                    bad_lines.add(n + 2)


# Filtering based on quality and saving the result

def quality(file, output_good, output_bad, quality_threshold, save_filtered, good_lines, bad_lines):
    with open(file) as file:
        count = 0
        n = 0 
        for line in file:
            count += 1
            n += 1
            if count == 4:
                count = 0
                quality_sequence = line.strip()
                s = 0
                for i in quality_sequence:
                    s += (ord(i) - 33)
                mean = s/len(quality_sequence)
                if mean < quality_threshold and n in good_lines:
                    good_lines.remove(n - 3)
                    good_lines.remove(n - 2)
                    good_lines.remove(n - 1)
                    good_lines.remove(n)
                    if save_filtered is True:
                        bad_lines.add(n - 3)
                        bad_lines.add(n - 2)
                        bad_lines.add(n - 1)
                        bad_lines.add(n)
    with open(file) as file:
        with open(output_good, "w") as out:
            n = 0
            for line in file:
                n += 1
                if n in good_lines:
                    out.write(line)
    if save_filtered is True:
        with open(file) as file:
            with open(output_bad, "w") as out:
                n = 0
                for line in file:
                    n += 1
                    if n in bad_lines:
                        out.write(line)


# Main function

def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False):
    file = input_fastq
    output_good = output_file_prefix + "_passed.fastq"
    output_bad = output_file_prefix + "_failed.fastq"
    good_lines = set()
    bad_lines = set()
    len_and_gc(file, length_bounds, gc_bounds,save_filtered, good_lines, bad_lines)
    quality(file, output_good, output_bad, quality_threshold, save_filtered, good_lines, bad_lines)


print("Enter path to fastq file: ")
input_fastq = input()
print("Enter file prefix to output file: ")
output_file_prefix = input()
print("Enter gc_content_bounds: ")
gc_bounds = tuple(float(i) for i in input().split())
print("Enter length_bounds: ")
length_bounds = tuple(int(i) for i in input().split())
print("Enter the minimal mean quality: ")
quality_threshold = input()
try:
  quality_threshold_in = float(quality_threshold_in)
except ValueError:
  pass
print("Do you want to save failed reads? Yes - 1, No - 0")
main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered=False)
