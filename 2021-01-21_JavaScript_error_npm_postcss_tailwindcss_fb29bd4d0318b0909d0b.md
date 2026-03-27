<!--
title:   [TailwindCSS] Error: PostCSS plugin tailwindcss requires PostCSS 8.
tags:    JavaScript,error,npm,postcss,tailwindcss
id:      fb29bd4d0318b0909d0b
private: false
-->
## エラー発生状況
Gatsbyで制作を進めていたサイトにTailwindを導入しようとした（21年1月時点）

```
PostCSS plugin postcss-nested requires PostCSS 8.
Migration guide for end-users:
https://github.com/postcss/postcss/wiki/PostCSS-8-for-end-users
```

## 対処
一度アンインストールして、互換性ビルドを再インストール

```
npm uninstall tailwindcss postcss autoprefixer
npm install tailwindcss@npm:@tailwindcss/postcss7-compat @tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9
```

## 原因
PostCSS8対応が追いついていないという感じでしょうか。
サポートされたら`latest`使ってくれとのこと。

## 参照
[PostCSS 7 compatibility build
](https://tailwindcss.com/docs/installation#post-css-7-compatibility-build)[PostCSS plugin postcss-nested requires PostCSS 8 #2799
](https://github.com/tailwindlabs/tailwindcss/issues/2799)