class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows>=len(s) or numRows==1:
            return s

        row = 0
        rows = [""]*numRows
        direction = -1

        for c in s:

            rows[row] += c
            if row==0 or row==numRows-1:
                direction *= -1


            row += direction
        
        return "".join(rows)



        
       



