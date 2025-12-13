class Solution:
    def defangIPaddr(self, address: str) -> str:
        val = ""
        for i in range(len(address)):
            if address[i] == ".":
                val += str("[.]")
            else:
                val += str(address[i])
        return val

        