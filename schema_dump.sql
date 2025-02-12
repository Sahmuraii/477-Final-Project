PGDMP                      |           db_FinalProject    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32834    db_FinalProject    DATABASE     �   CREATE DATABASE "db_FinalProject" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
 !   DROP DATABASE "db_FinalProject";
                postgres    false            �            1259    32857    allbookdata    TABLE     D  CREATE TABLE public.allbookdata (
    isbnid character varying(255),
    title character varying(255),
    author character varying(255),
    publicationyear integer,
    publisher character varying(255),
    imagelink1 character varying(255),
    imagelink2 character varying(255),
    imagelink3 character varying(255)
);
    DROP TABLE public.allbookdata;
       public         heap    postgres    false            �            1259    32932    author    TABLE     e   CREATE TABLE public.author (
    authorid integer NOT NULL,
    authorname character varying(255)
);
    DROP TABLE public.author;
       public         heap    postgres    false            �            1259    32931    author_authorid_seq    SEQUENCE     �   CREATE SEQUENCE public.author_authorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.author_authorid_seq;
       public          postgres    false    222            �           0    0    author_authorid_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.author_authorid_seq OWNED BY public.author.authorid;
          public          postgres    false    221            �            1259    32867    book    TABLE     ~   CREATE TABLE public.book (
    bookid integer NOT NULL,
    isbnid character varying(20),
    title character varying(255)
);
    DROP TABLE public.book;
       public         heap    postgres    false            �            1259    32866    book_bookid_seq    SEQUENCE     �   CREATE SEQUENCE public.book_bookid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.book_bookid_seq;
       public          postgres    false    219            �           0    0    book_bookid_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.book_bookid_seq OWNED BY public.book.bookid;
          public          postgres    false    218            �            1259    32926 
   bookauthor    TABLE     _   CREATE TABLE public.bookauthor (
    bookid integer NOT NULL,
    authorid integer NOT NULL
);
    DROP TABLE public.bookauthor;
       public         heap    postgres    false            �            1259    32966    bookpublisher    TABLE     e   CREATE TABLE public.bookpublisher (
    bookid integer NOT NULL,
    publisherid integer NOT NULL
);
 !   DROP TABLE public.bookpublisher;
       public         heap    postgres    false            �            1259    32950 	   publisher    TABLE     n   CREATE TABLE public.publisher (
    publisherid integer NOT NULL,
    publishername character varying(255)
);
    DROP TABLE public.publisher;
       public         heap    postgres    false            �            1259    32949    publisher_publisherid_seq    SEQUENCE     �   CREATE SEQUENCE public.publisher_publisherid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.publisher_publisherid_seq;
       public          postgres    false    224            �           0    0    publisher_publisherid_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.publisher_publisherid_seq OWNED BY public.publisher.publisherid;
          public          postgres    false    223            �            1259    32851    rating    TABLE     h   CREATE TABLE public.rating (
    userid integer,
    isbn character varying(255),
    rating integer
);
    DROP TABLE public.rating;
       public         heap    postgres    false            �            1259    32848    userdata    TABLE     k   CREATE TABLE public.userdata (
    userid integer,
    location character varying(255),
    age integer
);
    DROP TABLE public.userdata;
       public         heap    postgres    false            9           2604    32935    author authorid    DEFAULT     r   ALTER TABLE ONLY public.author ALTER COLUMN authorid SET DEFAULT nextval('public.author_authorid_seq'::regclass);
 >   ALTER TABLE public.author ALTER COLUMN authorid DROP DEFAULT;
       public          postgres    false    222    221    222            8           2604    32870    book bookid    DEFAULT     j   ALTER TABLE ONLY public.book ALTER COLUMN bookid SET DEFAULT nextval('public.book_bookid_seq'::regclass);
 :   ALTER TABLE public.book ALTER COLUMN bookid DROP DEFAULT;
       public          postgres    false    219    218    219            :           2604    32953    publisher publisherid    DEFAULT     ~   ALTER TABLE ONLY public.publisher ALTER COLUMN publisherid SET DEFAULT nextval('public.publisher_publisherid_seq'::regclass);
 D   ALTER TABLE public.publisher ALTER COLUMN publisherid DROP DEFAULT;
       public          postgres    false    223    224    224            @           2606    32937    author author_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (authorid);
 <   ALTER TABLE ONLY public.author DROP CONSTRAINT author_pkey;
       public            postgres    false    222            <           2606    32872    book book_bookid_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_bookid_key UNIQUE (bookid);
 >   ALTER TABLE ONLY public.book DROP CONSTRAINT book_bookid_key;
       public            postgres    false    219            >           2606    32930    bookauthor bookauthor_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.bookauthor
    ADD CONSTRAINT bookauthor_pkey PRIMARY KEY (bookid, authorid);
 D   ALTER TABLE ONLY public.bookauthor DROP CONSTRAINT bookauthor_pkey;
       public            postgres    false    220    220            D           2606    32970     bookpublisher bookpublisher_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.bookpublisher
    ADD CONSTRAINT bookpublisher_pkey PRIMARY KEY (bookid, publisherid);
 J   ALTER TABLE ONLY public.bookpublisher DROP CONSTRAINT bookpublisher_pkey;
       public            postgres    false    225    225            B           2606    32955    publisher publisher_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.publisher
    ADD CONSTRAINT publisher_pkey PRIMARY KEY (publisherid);
 B   ALTER TABLE ONLY public.publisher DROP CONSTRAINT publisher_pkey;
       public            postgres    false    224           