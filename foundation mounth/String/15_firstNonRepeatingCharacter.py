
'''
DEFINE countOf(s, n, target)
    SET count as 0
    FOR i from 0 to n-1
        IF s[i] = target
            SET count as count + 1
        END IF
    END FOR
    RETURN count
END DEFINE
DEFINE firstNonRepeatingCharacter(s, n)
    FOR i from 0 to n-1
        SET c1 as countOf(s, n, s[i])
        IF c1 = 1
            RETURN s[i]
        END IF
    END FOR
    RETURN '?'
END DEFINE
START PROGRAM
    READ s
    SET n as len(s)
    SET result as firstNonRepeatingCharacter(s, n)
    PRINT result
END PROGRAM
'''
