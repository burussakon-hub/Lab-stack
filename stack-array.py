class MyStack:
    def __init__(self, n):
        self.capacity = n              # ความจุสูงสุดของ stack
        self.arr = [0] * n             # อาร์เรย์สำหรับเก็บข้อมูล
        self.top = -1                  # ดัชนีของสมาชิกตัวบนสุด (-1 คือว่าง)

    def push(self, x):
        # TODO: เพิ่ม x ไว้ด้านบนสุดของ stack (ถ้าเต็มอยู่ไม่ต้องทำอะไร)
        if self.isFull():
            return 
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        # TODO: นำสมาชิกตัวบนสุดออก (ถ้าว่างอยู่ไม่ต้องทำอะไร)
        if self.isEmpty():
            return
        self.top -= 1

    def peek(self):
        # TODO: คืนค่าตัวบนสุด ถ้าว่างให้คืน -1
        if self.isEmpty():
            return -1
        return self.arr[self.top]

    def isEmpty(self):
        # TODO: คืน True ถ้า stack ว่าง มิฉะนั้นคืน False
        return self.top == -1

    def isFull(self):
        # TODO: คืน True ถ้า stack เต็ม มิฉะนั้นคืน False
        return self.top == self.capacity - 1


# ---------- Driver code: ห้ามแก้ไขส่วนนี้ ----------
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    st = MyStack(n)
    out = []
    for _ in range(q):
        op = int(data[idx]); idx += 1
        if op == 1:
            x = int(data[idx]); idx += 1
            st.push(x)
        elif op == 2:
            st.pop()
        elif op == 3:
            out.append(str(st.peek()))
        elif op == 4:
            out.append("true" if st.isEmpty() else "false")
        elif op == 5:
            out.append("true" if st.isFull() else "false")
    print(" ".join(out))


if __name__ == "__main__":
    main()