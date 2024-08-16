import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return -1
    
    bad_char = {}
    
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while(s <= n - m):
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
            s += (m - bad_char.get(text[s + m], -1) if s + m < n else 1)
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return -1

# Алгоритм Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    lps = [0] * m
    j = 0
    
    compute_lps(pattern, m, lps)
    
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

def compute_lps(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    hpattern = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == hpattern:
            if text[i:i + m] == pattern:
                return i
    return -1

# Читання текстів
with open('стаття 1.txt', 'r', encoding='windows-1251') as file:
    text1 = file.read()

with open('стаття 2.txt', 'r', encoding='windows-1251') as file:
    text2 = file.read()

# Тестові підрядки
pattern_exists = "алгоритм"  # підрядок, який існує
pattern_not_exists = "неіснуючийпідрядок"  # підрядок, якого немає

# Вимірювання часу для кожного алгоритму на першому тексті
time_bm_text1_exist = timeit.timeit(lambda: boyer_moore(text1, pattern_exists), number=100)
time_bm_text1_not_exist = timeit.timeit(lambda: boyer_moore(text1, pattern_not_exists), number=100)

time_kmp_text1_exist = timeit.timeit(lambda: kmp_search(text1, pattern_exists), number=100)
time_kmp_text1_not_exist = timeit.timeit(lambda: kmp_search(text1, pattern_not_exists), number=100)

time_rk_text1_exist = timeit.timeit(lambda: rabin_karp(text1, pattern_exists), number=100)
time_rk_text1_not_exist = timeit.timeit(lambda: rabin_karp(text1, pattern_not_exists), number=100)

# Вимірювання часу для кожного алгоритму на другому тексті
time_bm_text2_exist = timeit.timeit(lambda: boyer_moore(text2, pattern_exists), number=100)
time_bm_text2_not_exist = timeit.timeit(lambda: boyer_moore(text2, pattern_not_exists), number=100)

time_kmp_text2_exist = timeit.timeit(lambda: kmp_search(text2, pattern_exists), number=100)
time_kmp_text2_not_exist = timeit.timeit(lambda: kmp_search(text2, pattern_not_exists), number=100)

time_rk_text2_exist = timeit.timeit(lambda: rabin_karp(text2, pattern_exists), number=100)
time_rk_text2_not_exist = timeit.timeit(lambda: rabin_karp(text2, pattern_not_exists), number=100)

# Визначення найшвидшого алгоритму
def find_fastest(times):
    min_time = min(times)
    if min_time == times[0]:
        return "Boyer-Moore"
    elif min_time == times[1]:
        return "KMP"
    else:
        return "Rabin-Karp"

# Виведення результатів
print(f"Time for Boyer-Moore on text 1 (exists): {time_bm_text1_exist}")
print(f"Time for Boyer-Moore on text 1 (not exists): {time_bm_text1_not_exist}")
print(f"Time for KMP on text 1 (exists): {time_kmp_text1_exist}")
print(f"Time for KMP on text 1 (not exists): {time_kmp_text1_not_exist}")
print(f"Time for Rabin-Karp on text 1 (exists): {time_rk_text1_exist}")
print(f"Time for Rabin-Karp on text 1 (not exists): {time_rk_text1_not_exist}")

print(f"\nFastest algorithm for text 1 (exists): {find_fastest([time_bm_text1_exist, time_kmp_text1_exist, time_rk_text1_exist])}")
print(f"Fastest algorithm for text 1 (not exists): {find_fastest([time_bm_text1_not_exist, time_kmp_text1_not_exist, time_rk_text1_not_exist])}")

print(f"\nTime for Boyer-Moore on text 2 (exists): {time_bm_text2_exist}")
print(f"Time for Boyer-Moore on text 2 (not exists): {time_bm_text2_not_exist}")
print(f"Time for KMP on text 2 (exists): {time_kmp_text2_exist}")
print(f"Time for KMP on text 2 (not exists): {time_kmp_text2_not_exist}")
print(f"Time for Rabin-Karp on text 2 (exists): {time_rk_text2_exist}")
print(f"Time for Rabin-Karp on text 2 (not exists): {time_rk_text2_not_exist}")

print(f"\nFastest algorithm for text 2 (exists): {find_fastest([time_bm_text2_exist, time_kmp_text2_exist, time_rk_text2_exist])}")
print(f"Fastest algorithm for text 2 (not exists): {find_fastest([time_bm_text2_not_exist, time_kmp_text2_not_exist, time_rk_text2_not_exist])}")
