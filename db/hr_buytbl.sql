CREATE TABLE hr.buytbl (
    idnum NUMBER(8) NOT NULL PRIMARY KEY,
    userid CHAR(8) NOT NULL,
    prodname NCHAR(8) NOT NULL,
    groupname NCHAR(4),
    price NUMBER(8) NOT NULL,
    amount NUMBER(3) NOT NULL,
    FOREIGN KEY(userid) REFERENCES hr.usertbl(userid)
);

DECLARE
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM user_sequences
    WHERE sequence_name = 'IDSEQ';

    IF v_count > 0 THEN
        EXECUTE IMMEDIATE 'DROP SEQUENCE IDSEQ';
    END IF;
END;
/

CREATE SEQUENCE IDSEQ
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'KBS', '운동화', NULL, 30, 2);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'KBS', '노트', '전자', 1000, 1);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'JYP', '모니터', '전자', 200, 1);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'BBK', '모니터', '전자', 200, 5);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'KBS', '청바지', '의류', 50, 3);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'BBK', '메모리', '전자', 80, 10);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'SSK', '책', '서적', 15, 5);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'EJW', '책', '서적', 15, 2);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'EJW', '청바지', '의류', 50, 1);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'BBK', '운동화', NULL, 30, 2);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'EJW', '책', '서적', 15, 1);
INSERT INTO hr.buytbl VALUES (IDSEQ.NEXTVAL, 'BBK', '운동화', NULL, 30, 2);

