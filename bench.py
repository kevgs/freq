import os, subprocess, time

if os.name != 'nt':
	print("sorry, Windows only for now")
	os.exit(0)

def run1(args, PROG = '', RUNS = 10):
	if PROG == '':
		PROG = os.path.basename(args[-1])
	t = []
	for i in range(RUNS):
		tm = time.perf_counter()
		r = subprocess.Popen(args + ['pg.txt', 'out.txt'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		r.wait()
		t.append(time.perf_counter() - tm)
	t = sorted(t)
	print('%.3f..%.3fs %s' % (t[0], t[-1], PROG))

run1(['./x64/Release/freq01.exe'], 'freq01.cpp')
run1(['./freq01.exe'], 'freq01.go')
run1(['./rust/target/release/freq.exe'], 'rust/src/main.rs')
run1(['php', 'freq01.php'], RUNS=1)
