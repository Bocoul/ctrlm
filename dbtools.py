def db_copytable(filename, table1, table2):
    import sqlite3
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        res = cur.execute(
            """
            INSERT INTO "{}" ("rae", "code_postal", "commune", "code_insee", "siren", "voie") 
            SELECT DISTINCT "rae", "code_postal", "commune", "code_insee", "siren", "voie" FROM "{}";
            """.format(table1, table2))


if __name__ == "__main__":
    db_copytable("db_old/ctrlm.db", "ctrlm_pdl", "pdl")