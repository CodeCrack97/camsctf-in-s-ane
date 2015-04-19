import struct
carve = """89 50 4e
47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00 00
14 00 00 00 14 08 06 00 00 01 fa 8e 2d 9b 00 00
00 19 74 45 58 74 53 6f 66 74 77 61 72 65 00 41
64 6f 62 65 20 49 6d 61 67 65 52 65 61 64 79 71
c9 65 3c 00 00 03 68 69 54 58 74 58 4d 4c 3a 63
6f 6d 2e 61 64 6f 62 65 2e 78 6d 70 00 00 00 00
00 3c 3f 78 70 61 63 6b 65 74 20 62 65 67 69 6e
3d 22 ef bb bf 22 20 69 64 3d 22 57 35 4d 30 4d
70 43 65 68 69 48 7a 72 65 53 7a 4e 54 63 7a 6b
63 39 64 22 3f 3e 20 3c 78 3a 78 6d 70 6d 65 74
61 20 78 6d 6c 6e 73 3a 78 3d 22 61 64 6f 62 65
3a 6e 73 3a 6d 65 74 61 2f 22 20 78 3a 78 6d 70
74 6b 3d 22 41 64 6f 62 65 20 58 4d 50 20 43 6f
72 65 20 35 2e 35 2d 63 30 32 31 20 37 39 2e 31
35 35 37 37 32 2c 20 32 30 31 34 2f 30 31 2f 31
33 2d 31 39 3a 34 34 3a 30 30 20 20 20 20 20 20
20 20 22 3e 20 3c 72 64 66 3a 52 44 46 20 78 6d
6c 6e 73 3a 72 64 66 3d 22 68 74 74 70 3a 2f 2f
77 77 77 2e 77 33 2e 6f 72 67 2f 31 39 39 39 2f
30 32 2f 32 32 2d 72 64 66 2d 73 79 6e 74 61 78
2d 6e 73 23 22 3e 20 3c 72 64 66 3a 44 65 73 63
72 69 70 74 69 6f 6e 20 72 64 66 3a 61 62 6f 75
74 3d 22 22 20 78 6d 6c 6e 73 3a 78 6d 70 4d 4d
3d 22 68 74 74 70 3a 2f 2f 6e 73 2e 61 64 6f 62
65 2e 63 6f 6d 2f 78 61 70 2f 31 2e 30 2f 6d 6d
2f 22 20 78 6d 6c 6e 73 3a 73 74 52 65 66 3d 22
68 74 74 70 3a 2f 2f 6e 73 2e 61 64 6f 62 65 2e
63 6f 6d 2f 78 61 70 2f 31 2e 30 2f 73 54 79 70
65 2f 52 65 73 6f 75 72 63 65 52 65 66 23 22 20
78 6d 6c 6e 73 3a 78 6d 70 3d 22 68 74 74 70 3a
2f 2f 6e 73 2e 61 64 6f 62 65 2e 63 6f 6d 2f 78
61 70 2f 31 2e 30 2f 22 20 78 6d 70 4d 4d 3a 4f
72 69 67 69 6e 61 6c 44 6f 63 75 6d 65 6e 74 49
44 3d 22 78 6d 70 2e 64 69 64 3a 30 36 38 30 31
31 37 34 30 37 32 30 36 38 31 31 38 41 36 44 44
42 34 43 44 37 39 36 38 42 44 32 22 20 78 6d 70
4d 4d 3a 44 6f 63 75 6d 65 6e 74 49 44 3d 22 78
6d 70 2e 64 69 64 3a 32 38 30 32 30 31 31 44 35
38 38 35 31 31 45 34 39 34 33 44 39 33 42 44 35
39 32 39 41 30 30 35 22 20 78 6d 70 4d 4d 3a 49
6e 73 74 61 6e 63 65 49 44 3d 22 78 6d 70 2e 69
69 64 3a 32 38 30 32 30 31 31 43 35 38 38 35 31
31 45 34 39 34 33 44 39 33 42 44 35 39 32 39 41
30 30 35 22 20 78 6d 70 3a 43 72 65 61 74 6f 72
54 6f 6f 6c 3d 22 41 64 6f 62 65 20 50 68 6f 74
6f 73 68 6f 70 20 43 53 36 20 28 4d 61 63 69 6e
74 6f 73 68 29 22 3e 20 3c 78 6d 70 4d 4d 3a 44
65 72 69 76 65 64 46 72 6f 6d 20 73 74 52 65 66
3a 69 6e 73 74 61 6e 63 65 49 44 3d 22 78 6d 70
2e 69 69 64 3a 33 46 45 42 41 44 34 32 35 38 37
38 31 31 45 34 39 34 33 44 39 33 42 44 35 39 32
39 41 30 30 35 22 20 73 74 52 65 66 3a 64 6f 63
75 6d 65 6e 74 49 44 3d 22 78 6d 70 2e 64 69 64
3a 33 46 45 42 41 44 34 33 35 38 37 38 31 31 45
34 39 34 33 44 39 33 42 44 35 39 32 39 41 30 30
35 22 2f 3e 20 3c 2f 72 64 66 3a 44 65 73 63 72
69 70 74 69 6f 6e 3e 20 3c 2f 72 64 66 3a 52 44
46 3e 20 3c 2f 78 3a 78 6d 70 6d 65 74 61 3e 20
3c 3f 78 70 61 63 6b 65 74 20 65 6e 64 3d 22 72
22 3f 3e 3d f0 84 01 00 00 02 33 49 44 41 54 78
da 62 fc ff ff 3f 03 0c b0 80 88 ce ce 4e 5e 20
f5 89 09 2a 58 00 c4 8c 00 01 c4 08 53 c6 cc c9
c9 c9 70 f4 e8 d1 48 90 34 1f 10 2f 03 08 20 b0
14 50 d3 49 20 87 0d 88 75 80 58 98 05 aa d9 0c
a4 19 88 41 9a ef 03 04 10 23 b2 5d 70 3b 81 5a
41 74 17 10 97 81 54 96 97 97 33 82 b4 df 07 62
45 a8 56 90 11 0c 20 1b 77 43 05 d6 02 f1 64 98
60 1a d4 a8 60 20 16 02 31 00 02 08 e6 24 06 24
57 ac 04 62 69 20 5e 00 d3 00 b4 87 81 09 49 41
2e 10 bb 01 b1 29 10 1f 02 e2 54 a8 dc 7f 78 c8
00 c1 11 a8 63 82 a1 6c 75 20 be 07 f5 78 3b cc
3d 0c 50 01 90 a6 8d 40 ac 01 c4 13 81 58 09 88
7f 02 b1 3c dc 8d c4 00 80 00 22 5a 21 2c f6 60
fc 59 40 9c 00 c4 4f 81 38 1c 88 4f a1 fb 1a 14
7d bf 80 58 17 88 9d 80 d8 08 88 4f 42 31 03 b2
67 3e 42 3d 74 07 88 05 a1 26 82 3c f6 0e 1a 74
f0 e0 e9 85 d2 b1 50 c5 9c 40 1c 00 c4 5e d0 08
50 84 29 2c 86 46 15 07 10 2b 43 c5 40 01 3e 1b
1a 4b 70 ab 41 20 11 aa 98 11 c9 63 02 d0 a8 84
5b bd 0c 88 a3 80 58 02 2d 54 de c3 34 c2 14 46
43 69 67 58 dc 42 01 3f c9 01 0e 10 60 44 2b 24
16 c0 9c 88 1c 8b a0 48 9a 0e f5 1b 08 1c 00 e2
2d 40 2c 0e c4 a1 40 ac 80 e4 ff 4c 50 be 85 c5
32 7a 28 82 c0 52 20 7e 03 c4 f3 81 d8 02 88 af
42 35 b0 43 33 9f 27 10 ff 03 e2 5b d0 d0 fd 08
d5 83 e9 42 68 34 98 40 23 f9 2f 54 0e c4 ff 01
cd 9f c8 61 b3 0b 9a 77 ab 81 b8 15 88 bf c2 72
21 b2 0b 13 a0 de d5 82 f2 41 99 6b 0e d4 85 41
48 ea c2 a1 b9 95 01 9a e9 8e 42 f5 62 78 f9 29
34 3d 5c 82 ba e6 12 d4 5b 20 4b 4a 90 d4 ad 84
ca 47 42 e9 c7 50 bd 18 06 86 a3 85 27 48 ae 07
29 ed 47 a3 c9 77 00 f1 1e 20 8e 40 d6 8b 6c e0
29 68 c2 3b 85 25 35 14 a0 07 3e 10 c8 01 31 2f
ba 1e 16 34 45 a0 f0 32 47 2a d9 52 a0 a5 29 28
63 fd 86 7a 6d 37 34 6c 4f d1 25 61 03 00 df ee
91 44 b4 6c ff e1 00 00 00 00 49 45 4e 44 ae 42
60 82"""
out = open('carved2.png', 'wb')
h = ''
for byte in carve.replace('\n', ' ').split(' '):
    h+=struct.pack('!B', int(byte, 16))
out.write(h)
out.close()
