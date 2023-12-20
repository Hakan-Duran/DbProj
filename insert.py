def insert(table, request):
    if table == "co2_production":
        ISO3 = request.form['ISO3']
        Country = request.form['Country']
        hdicode = request.form['hdicode']
        region = request.form['region']
        hdi_rank_2021 = request.form['hdi_rank_2021']
        co2_prod_1990 = request.form['co2_prod_1990']
        co2_prod_1991 = request.form['co2_prod_1991']
        co2_prod_1992 = request.form['co2_prod_1992']
        co2_prod_1993 = request.form['co2_prod_1993']
        co2_prod_1994 = request.form['co2_prod_1994']
        co2_prod_1995 = request.form['co2_prod_1995']
        co2_prod_1996 = request.form['co2_prod_1996']
        co2_prod_1997 = request.form['co2_prod_1997']
        co2_prod_1998 = request.form['co2_prod_1998']
        co2_prod_1999 = request.form['co2_prod_1999']
        co2_prod_2000 = request.form['co2_prod_2000']
        co2_prod_2001 = request.form['co2_prod_2001']
        co2_prod_2002 = request.form['co2_prod_2002']
        co2_prod_2003 = request.form['co2_prod_2003']
        co2_prod_2004 = request.form['co2_prod_2004']
        co2_prod_2005 = request.form['co2_prod_2005']
        co2_prod_2006 = request.form['co2_prod_2006']
        co2_prod_2007 = request.form['co2_prod_2007']
        co2_prod_2008 = request.form['co2_prod_2008']
        co2_prod_2009 = request.form['co2_prod_2009']
        co2_prod_2010 = request.form['co2_prod_2010']
        co2_prod_2011 = request.form['co2_prod_2011']
        co2_prod_2012 = request.form['co2_prod_2012']
        co2_prod_2013 = request.form['co2_prod_2013']
        co2_prod_2014 = request.form['co2_prod_2014']
        co2_prod_2015 = request.form['co2_prod_2015']
        co2_prod_2016 = request.form['co2_prod_2016']
        co2_prod_2017 = request.form['co2_prod_2017']
        co2_prod_2018 = request.form['co2_prod_2018']
        co2_prod_2019 = request.form['co2_prod_2019']
        co2_prod_2020 = request.form['co2_prod_2020']
        co2_prod_2021 = request.form['co2_prod_2021']
        
        query = f"""INSERT INTO co2_production ( 
            ISO3, Country, hdicode, region, hdi_rank_2021, co2_prod_1990, co2_prod_1991, co2_prod_1992, co2_prod_1993, co2_prod_1994, co2_prod_1995, co2_prod_1996, co2_prod_1997, 
            co2_prod_1998, co2_prod_1999, co2_prod_2000, co2_prod_2001, co2_prod_2002, co2_prod_2003, co2_prod_2004, co2_prod_2005, co2_prod_2006, co2_prod_2007, co2_prod_2008, co2_prod_2009,
            co2_prod_2010, co2_prod_2011, co2_prod_2012, co2_prod_2013, co2_prod_2014, co2_prod_2015, co2_prod_2016, co2_prod_2017, co2_prod_2018, co2_prod_2019, co2_prod_2020, co2_prod_2021
            )
            VALUES (
            '{ISO3}', '{Country}', '{hdicode}', '{region}', {hdi_rank_2021}, {co2_prod_1990}, {co2_prod_1991}, {co2_prod_1992}, 
            {co2_prod_1993}, {co2_prod_1994}, {co2_prod_1995}, {co2_prod_1996}, {co2_prod_1997}, 
            {co2_prod_1998}, {co2_prod_1999}, {co2_prod_2000}, {co2_prod_2001}, {co2_prod_2002}, {co2_prod_2003}, 
            {co2_prod_2004}, {co2_prod_2005}, {co2_prod_2006}, {co2_prod_2007}, {co2_prod_2008}, {co2_prod_2009},
            {co2_prod_2010}, {co2_prod_2011}, {co2_prod_2012}, {co2_prod_2013}, {co2_prod_2014}, {co2_prod_2015}, 
            {co2_prod_2016}, {co2_prod_2017}, {co2_prod_2018}, {co2_prod_2019}, {co2_prod_2020}, {co2_prod_2021}1
            );
        """
        return query

    if table == "gross_national_income_per_capita":
        ISO3 = request.form['ISO3']
        Country = request.form['Country']
        hdicode = request.form['hdicode']
        region = request.form['region']
        hdi_rank_2021 = request.form['hdi_rank_2021']
        gnipc_1990 = request.form['gnipc_1990']
        gnipc_1991 = request.form['gnipc_1991']
        gnipc_1992 = request.form['gnipc_1992']
        gnipc_1993 = request.form['gnipc_1993']
        gnipc_1994 = request.form['gnipc_1994']
        gnipc_1995 = request.form['gnipc_1995']
        gnipc_1996 = request.form['gnipc_1996']
        gnipc_1997 = request.form['gnipc_1997']
        gnipc_1998 = request.form['gnipc_1998']
        gnipc_1999 = request.form['gnipc_1999']
        gnipc_2000 = request.form['gnipc_2000']
        gnipc_2001 = request.form['gnipc_2001']
        gnipc_2002 = request.form['gnipc_2002']
        gnipc_2003 = request.form['gnipc_2003']
        gnipc_2004 = request.form['gnipc_2004']
        gnipc_2005 = request.form['gnipc_2005']
        gnipc_2006 = request.form['gnipc_2006']
        gnipc_2007 = request.form['gnipc_2007']
        gnipc_2008 = request.form['gnipc_2008']
        gnipc_2009 = request.form['gnipc_2009']
        gnipc_2010 = request.form['gnipc_2010']
        gnipc_2011 = request.form['gnipc_2011']
        gnipc_2012 = request.form['gnipc_2012']
        gnipc_2013 = request.form['gnipc_2013']
        gnipc_2014 = request.form['gnipc_2014']
        gnipc_2015 = request.form['gnipc_2015']
        gnipc_2016 = request.form['gnipc_2016']
        gnipc_2017 = request.form['gnipc_2017']
        gnipc_2018 = request.form['gnipc_2018']
        gnipc_2019 = request.form['gnipc_2019']
        gnipc_2020 = request.form['gnipc_2020']
        gnipc_2021 = request.form['gnipc_2021']
        
        query = f"""INSERT INTO gross_national_income_per_capita ( 
            ISO3, Country, hdicode, region, hdi_rank_2021, gnipc_1990, gnipc_1991, gnipc_1992, gnipc_1993, gnipc_1994, gnipc_1995, gnipc_1996, gnipc_1997, 
            gnipc_1998, gnipc_1999, gnipc_2000, gnipc_2001, gnipc_2002, gnipc_2003, gnipc_2004, gnipc_2005, gnipc_2006, gnipc_2007, gnipc_2008, gnipc_2009,
            gnipc_2010, gnipc_2011, gnipc_2012, gnipc_2013, gnipc_2014, gnipc_2015, gnipc_2016, gnipc_2017, gnipc_2018, gnipc_2019, gnipc_2020, gnipc_2021
            )
            VALUES (
            '{ISO3}', '{Country}', '{hdicode}', '{region}', {hdi_rank_2021}, {gnipc_1990}, {gnipc_1991}, {gnipc_1992}, 
            {gnipc_1993}, {gnipc_1994}, {gnipc_1995}, {gnipc_1996}, {gnipc_1997}, 
            {gnipc_1998}, {gnipc_1999}, {gnipc_2000}, {gnipc_2001}, {gnipc_2002}, {gnipc_2003}, 
            {gnipc_2004}, {gnipc_2005}, {gnipc_2006}, {gnipc_2007}, {gnipc_2008}, {gnipc_2009},
            {gnipc_2010}, {gnipc_2011}, {gnipc_2012}, {gnipc_2013}, {gnipc_2014}, {gnipc_2015}, 
            {gnipc_2016}, {gnipc_2017}, {gnipc_2018}, {gnipc_2019}, {gnipc_2020}, {gnipc_2021}
            );
        """
        return query


    if table == "human_development_index":
        ISO3 = request.form['ISO3']
        Country = request.form['Country']
        hdicode = request.form['hdicode']
        region = request.form['region']
        hdi_rank_2021 = request.form['hdi_rank_2021']
        hdi_1990 = request.form['hdi_1990']
        hdi_1991 = request.form['hdi_1991']
        hdi_1992 = request.form['hdi_1992']
        hdi_1993 = request.form['hdi_1993']
        hdi_1994 = request.form['hdi_1994']
        hdi_1995 = request.form['hdi_1995']
        hdi_1996 = request.form['hdi_1996']
        hdi_1997 = request.form['hdi_1997']
        hdi_1998 = request.form['hdi_1998']
        hdi_1999 = request.form['hdi_1999']
        hdi_2000 = request.form['hdi_2000']
        hdi_2001 = request.form['hdi_2001']
        hdi_2002 = request.form['hdi_2002']
        hdi_2003 = request.form['hdi_2003']
        hdi_2004 = request.form['hdi_2004']
        hdi_2005 = request.form['hdi_2005']
        hdi_2006 = request.form['hdi_2006']
        hdi_2007 = request.form['hdi_2007']
        hdi_2008 = request.form['hdi_2008']
        hdi_2009 = request.form['hdi_2009']
        hdi_2010 = request.form['hdi_2010']
        hdi_2011 = request.form['hdi_2011']
        hdi_2012 = request.form['hdi_2012']
        hdi_2013 = request.form['hdi_2013']
        hdi_2014 = request.form['hdi_2014']
        hdi_2015 = request.form['hdi_2015']
        hdi_2016 = request.form['hdi_2016']
        hdi_2017 = request.form['hdi_2017']
        hdi_2018 = request.form['hdi_2018']
        hdi_2019 = request.form['hdi_2019']
        hdi_2020 = request.form['hdi_2020']
        hdi_2021 = request.form['hdi_2021']
        
        query = f"""INSERT INTO human_development_index ( 
            ISO3, Country, hdicode, region, hdi_rank_2021, hdi_1990, hdi_1991, hdi_1992, hdi_1993, hdi_1994, hdi_1995, hdi_1996, hdi_1997, 
            hdi_1998, hdi_1999, hdi_2000, hdi_2001, hdi_2002, hdi_2003, hdi_2004, hdi_2005, hdi_2006, hdi_2007, hdi_2008, hdi_2009,
            hdi_2010, hdi_2011, hdi_2012, hdi_2013, hdi_2014, hdi_2015, hdi_2016, hdi_2017, hdi_2018, hdi_2019, hdi_2020, hdi_2021
            )
            VALUES (
            '{ISO3}', '{Country}', '{hdicode}', '{region}', {hdi_rank_2021}, {hdi_1990}, {hdi_1991}, {hdi_1992}, 
            {hdi_1993}, {hdi_1994}, {hdi_1995}, {hdi_1996}, {hdi_1997}, 
            {hdi_1998}, {hdi_1999}, {hdi_2000}, {hdi_2001}, {hdi_2002}, {hdi_2003}, 
            {hdi_2004}, {hdi_2005}, {hdi_2006}, {hdi_2007}, {hdi_2008}, {hdi_2009},
            {hdi_2010}, {hdi_2011}, {hdi_2012}, {hdi_2013}, {hdi_2014}, {hdi_2015}, 
            {hdi_2016}, {hdi_2017}, {hdi_2018}, {hdi_2019}, {hdi_2020}, {hdi_2021}
            );
        """
        return query


    if table == "life_expectancy_by_birth":
        ISO3 = request.form['ISO3']
        Country = request.form['Country']
        hdicode = request.form['hdicode']
        region = request.form['region']
        hdi_rank_2021 = request.form['hdi_rank_2021']
        le_1990 = request.form['le_1990']
        le_1991 = request.form['le_1991']
        le_1992 = request.form['le_1992']
        le_1993 = request.form['le_1993']
        le_1994 = request.form['le_1994']
        le_1995 = request.form['le_1995']
        le_1996 = request.form['le_1996']
        le_1997 = request.form['le_1997']
        le_1998 = request.form['le_1998']
        le_1999 = request.form['le_1999']
        le_2000 = request.form['le_2000']
        le_2001 = request.form['le_2001']
        le_2002 = request.form['le_2002']
        le_2003 = request.form['le_2003']
        le_2004 = request.form['le_2004']
        le_2005 = request.form['le_2005']
        le_2006 = request.form['le_2006']
        le_2007 = request.form['le_2007']
        le_2008 = request.form['le_2008']
        le_2009 = request.form['le_2009']
        le_2010 = request.form['le_2010']
        le_2011 = request.form['le_2011']
        le_2012 = request.form['le_2012']
        le_2013 = request.form['le_2013']
        le_2014 = request.form['le_2014']
        le_2015 = request.form['le_2015']
        le_2016 = request.form['le_2016']
        le_2017 = request.form['le_2017']
        le_2018 = request.form['le_2018']
        le_2019 = request.form['le_2019']
        le_2020 = request.form['le_2020']
        le_2021 = request.form['le_2021']
        
        query = f"""INSERT INTO life_expectancy_by_birth ( 
            ISO3, Country, hdicode, region, hdi_rank_2021, le_1990, le_1991, le_1992, le_1993, le_1994, le_1995, le_1996, le_1997, 
            le_1998, le_1999, le_2000, le_2001, le_2002, le_2003, le_2004, le_2005, le_2006, le_2007, le_2008, le_2009,
            le_2010, le_2011, le_2012, le_2013, le_2014, le_2015, le_2016, le_2017, le_2018, le_2019, le_2020, le_2021
            )
            VALUES (
            '{ISO3}', '{Country}', '{hdicode}', '{region}', {hdi_rank_2021}, {le_1990}, {le_1991}, {le_1992}, 
            {le_1993}, {le_1994}, {le_1995}, {le_1996}, {le_1997}, 
            {le_1998}, {le_1999}, {le_2000}, {le_2001}, {le_2002}, {le_2003}, 
            {le_2004}, {le_2005}, {le_2006}, {le_2007}, {le_2008}, {le_2009},
            {le_2010}, {le_2011}, {le_2012}, {le_2013}, {le_2014}, {le_2015}, 
            {le_2016}, {le_2017}, {le_2018}, {le_2019}, {le_2020}, {le_2021}
            );
        """
        return query
