class Stack:
    """สแต็กมาตรฐาน ห้ามแก้ไขคลาสนี้"""

    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            return -1
        return self._data.pop()

    def peek(self):
        if not self._data:
            return -1
        return self._data[-1]

    def isEmpty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


class MyQueue:
    def __init__(self):
        self.s1 = Stack()   # สแต็กสำหรับรับข้อมูลเข้า
        self.s2 = Stack()   # สแต็กสำหรับนำข้อมูลออก

    def _transfer(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop)

    def enqueue(self, x):
        # TODO: เพิ่ม x ไว้ที่ท้ายคิว
        self.s1.push(x)

    def dequeue(self):
        # TODO: นำสมาชิกตัวหน้าสุดออก (ถ้าคิวว่างอยู่ไม่ต้องทำอะไร)
        self._transfer()
        if self.s2.isEmpty():
            return 
        self.s2.pop()

    def front(self):
        # TODO: คืนค่าตัวหน้าสุด ถ้าคิวว่างให้คืน -1
        self._transfer()
        return self.s2.peek()

    def size(self):
        # TODO: คืนจำนวนสมาชิกในคิว
        return self.s1.size() + self.s2.size()


# ---------- Driver code: ห้ามแก้ไขส่วนนี้ ----------
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    q = int(data[idx]); idx += 1
    qu = MyQueue()
    out = []
    for _ in range(q):
        op = int(data[idx]); idx += 1
        if op == 1:
            x = int(data[idx]); idx += 1
            qu.enqueue(x)
        elif op == 2:
            qu.dequeue()
        elif op == 3:
            out.append(str(qu.front()))
        elif op == 4:
            out.append(str(qu.size()))
    print(" ".join(out))


if __name__ == "__main__":
    main()