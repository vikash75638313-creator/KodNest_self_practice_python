

'''
1. Question kya hai?
Humein ek string di gayi hai. Humein us string mein se un 
characters ko print karna hai jo ek se zyada baar aate hain.

DEFINE countOf(s, n, target)
    SET count as 0
    FOR i from 0 to n-1
        IF s[i] = target
            SET count as count + 1
        END IF
    END FOR

    RETURN count
END DEFINE

DEFINE firstPositionOf(s, n, target)
    FOR i from 0 to n-1
        IF s[i] = target
            RETURN i
        END IF
    END FOR

    RETURN -1
END DEFINE

DEFINE printDuplicateCharacters(s, n)
    FOR i from 0 to n-1
        SET count as countOf(s, n, s[i])
        SET firstPosition as firstPositionOf(s, n, s[i])
        
        IF count > 1 AND i = firstPosition
            PRINT s[i]
        END IF
    END FOR
END DEFINE

START PROGRAM
    READ s
    SET n as len(s)
    CALL printDuplicateCharacters(s, n)
END PROGRAM
'''

